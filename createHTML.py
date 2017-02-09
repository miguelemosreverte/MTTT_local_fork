#!/usr/bin/env python
# -*- coding: utf-8 -*-
import libsemeval2014task5
import matplotlib.pyplot as plt
import glob
import os
import numpy as np

class Evaluator:
    def __init__(self,reference_filepath,mt_filepath):
        self.reference_filepath = reference_filepath
        self.mt_filepath = mt_filepath
        if (os.path.splitext(self.reference_filepath)[1] != '.xml'):
            self.to_xml("ref")

        if (os.path.splitext(self.mt_filepath)[1] != '.xml'):
            self.to_xml("output")

    def to_xml(self, option):

        if option == "output":
            filepath = self.mt_filepath
            self.mt_filepath += ".xml"
        if option == "ref":
             filepath = self.reference_filepath
             self.reference_filepath += ".xml"
        f = open(filepath + ".xml", 'w+');f.write("");f.close()

        id = 0
        with open(filepath) as f1, open(filepath +  ".xml", 'a') as f2:
            f2.write('<sentencepairs L1="en" L2="de">' + "\n")

            for line in f1:
                id += 1
                if option == "ref":
                    f2.write('<s category="a" source="EndStation C2 - Spiros Koukidis, Jörg Kassner, Andrea Näfken, Sabine Tews" id="'+str(id)+'">\n')
                if option == "output":
                    f2.write('<s id="%s">\n'%str(id))
                pre = '<input><f id="%s">'%str(id)
                post = '</input></f>'
                f2.write(pre + line.replace('\n','') + post + "\n")

                pre = '<%s><f id="%s">'% (option,str(id))
                post = '</%s></f>'%option
                f2.write(pre + line.replace('\n','') + post + "\n")
                f2.write('</s>' + "\n")

    def evaluate(self):
        os.chdir("./semeval2014task5/evaluation/")
        f = self.mt_filepath#"CNRC.en-de.run1.xml"

        fields = os.path.basename(f).split('.')
        team = self.mt_filepath.split(".")[:-1][0]
        print team
        L1, L2 = ['en','de']
        run = 'run1'

        eval = 'both'

        if eval == 'both' or eval == 'best':
            #BEST Evaluation
            print("Processing " + f  + " (BEST)")
            if eval == 'both':
                evalf = team + '.' + L1 + '-' + L2 + '.' + run + '.best.xml'
                os.rename(f, evalf) #temporary rename so output files will be consistently named
            else:
                evalf = f
            #cmd = "semeval2014task5-evaluate -I --ref " +             self.reference_filepath + " --out " + self.mt_filepath + "> " + "CNRC.en-de.run1.best.log" + " 2> /dev/null"
            cmd = "semeval2014task5-evaluate -I --ref    "+self.reference_filepath+" --out "+ evalf +"> "+ evalf.replace('.xml','.log') +" 2> /dev/null"
            print cmd
            r = os.system(cmd)
            if eval == 'both':
                os.rename(evalf, f) #undo temporary rename
            if r != 0:
                print("Failed prematurely!")
                return
        if eval == 'both' or eval == 'oof':
            #OOF Evaluation
            print("Processing " + f  + " (OOF)")
            if eval == 'both':
                evalf = team + '.' + L1 + '-' + L2 + '.' + run + '.oof.xml'
                os.rename(f, evalf)  #temporary rename so output files will be consistently named
            else:
                evalf = f
            print "evalf",evalf
            cmd = "semeval2014task5-evaluate -I -a --ref "+self.reference_filepath+" --out "+ evalf +"> "+ evalf.replace('.xml','.log') +" 2> /dev/null"
            r = os.system(cmd)
            if eval == 'both':
                os.rename(evalf, f) #undo temporary rename
            if r != 0:
                print("Failed prematurely!")
                return
        print("Done")
        os.chdir("../../")

    def read_score_summaries_into_memory(self):
        self.data = {}

        #Read score summaries into memory
        teams = set()
        for filename in glob.glob("semeval2014task5/evaluation/*.summary.score"):
            with open(filename) as f:
                print os.path.basename(filename).split('.',5)
                team, langs, run, evtype, _,_ = os.path.basename(filename).split('.',5)
                if not langs in self.data:
                    self.data[langs] = {}
                if not evtype in self.data[langs]:
                    self.data[langs][evtype] = {}
                if not team + '-' + run in self.data[langs][evtype]:
                    self.data[langs][evtype][team + '-' + run] = {}
                d = self.data[langs][evtype][team + '-' + run]
                teams.add(team)
                f.readline()
                d['ac'], d['wac'],d['rec'] = ( float(x) for x in f.readline().split(" ") )
        print self.data

    def createHTMLs(self):
        #Output graphs
        plt.rc('font', family='FreeSans')
        plt.rc('font', serif='Helvetica Neue')
        plt.rc('text', usetex='false')
        plt.rcParams.update({'font.size': 18})
        self.graph('en-de','best', "English (L1) - German (L2), Best")
        self.graph('en-de','oof', "English (L1) - German (L2), Out of Five")

        #Output Table
        s = ""
        for langs in sorted(self.data):
            for evtype in sorted(self.data[langs]):
                s += "<h2>" + langs + " (" + evtype + ")</h2>"
                s += "<table>"
                s += "<tr><th></th><th>Accuracy</th><th>Word Accuracy</th><th>Recall</th></tr>"
                for team, d in sorted(self.data[langs][evtype].items(), key=lambda x: -1 * x[1]['wac'] ):
                    s += "<tr><th>" + team + "</th><td>" + str(round(d['ac'],3)) + "</td><td>" + str(round(d['wac'],3)) + "</td><td>" + str(d['rec']) + "</tr>"
                s += "</table>"
        html_output_folder = os.path.abspath("HTML output/")
        if not os.path.exists(html_output_folder): os.makedirs(html_output_folder)
        with open(html_output_folder + "/" + "table" + '.html','w') as f: f.write(s)

    def start_evaluation_process(self):
        self.evaluate()
        self.read_score_summaries_into_memory()
        self.createHTMLs()

    def graph(self, langs, evtype, title=""):
        values = []
        teams = sorted(self.data[langs][evtype].keys())
        for team in teams:
            values.append(self.data[langs][evtype][team])

        index = np.arange(len(values))
        bar_width = 0.3

        my_dpi = 100
        fig = plt.figure(figsize=(600/my_dpi, 300/my_dpi), dpi=my_dpi)
        plt.bar(index, [x['ac'] for x in  values] , bar_width,color='#6071B3',label="Accuracy")
        plt.bar(index + bar_width, [x['wac'] for x in values], bar_width,color='#60B362',label="Word Accuracy")
        plt.bar(index + 2*bar_width, [x['rec'] for x in values], bar_width,color='#B36060',label="Recall")
        plt.xticks(index + bar_width, [x.replace("-","\n") for x in  teams])
        #plt.xlabel("Systems")
        plt.ylabel("Score")
        plt.grid()
        if title:
            plt.title(title, fontweight='bold')
        else:
            plt.title(langs + " (" + evtype + ")")
        #plt.legend()
        if not os.path.exists(os.path.abspath("HTML output/")): os.makedirs(os.path.abspath("HTML output/"))
        plt.savefig(os.path.abspath("HTML output/"+evtype + ".png"))

if __name__ == "__main__":
    evaluator = Evaluator("/home/migue/Desktop/news-commentary-v8.de","/home/migue/Desktop/news-commentary-v8.en")
