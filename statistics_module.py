
class Statistics:

    def __init__(self, source, target):
        self.source = source
        self.target = target

    def calculate_time_per_segment(self):
        seconds_spent_by_segment = {}
        percentaje_spent_by_segment = {}
        total_time_spent = 0
        #again with the closure, lets see how it plays out.
        def pairwise(iterable):
            a, b = itertools.tee(iterable)
            next(b, None)
            return itertools.izip(a, b)

        #calculate time spent by segment
        for current_timestamp,next_timestamp in pairwise(sorted(self.paulaslog.keys())):
            #for current_timestamp,next_timestamp in sorted(self.paulaslog.keys()):
            delta = (int(next_timestamp) - int(current_timestamp))/1000
            for segment_index in self.paulaslog[current_timestamp]:
                if segment_index in seconds_spent_by_segment:
                    seconds_spent_by_segment[segment_index] += delta
                else:
                    seconds_spent_by_segment[segment_index] = delta
        #calculate total time spent
        for a in seconds_spent_by_segment:
            total_time_spent += seconds_spent_by_segment[a]
        #calculate percentajes
        for a in seconds_spent_by_segment:
            percentaje_spent_by_segment[a] = float(seconds_spent_by_segment[a]) *100 / float(total_time_spent)


        title = "<th>Segment </th><th>" + '%'+ " of the time spent </th>"
        return self.build_pie_as_json_string(percentaje_spent_by_segment),self.build_table(percentaje_spent_by_segment),title

    def calculate_deletions_per_segment(self):
        percentaje_spent_by_segment=self.tables["translation_table"].calculate_insertions_or_deletions_percentajes(True)
        title = "<th>Segment </th><th>" + '%'+ " of deletions made</th>"
        return self.build_pie_as_json_string(percentaje_spent_by_segment),self.build_table(percentaje_spent_by_segment),title
    def calculate_insertions_per_segment(self):
        percentaje_spent_by_segment=self.tables["translation_table"].calculate_insertions_or_deletions_percentajes(False)
        title = "<th>Segment </th><th>" + '%'+ " of insertions made</th>"
        return self.build_pie_as_json_string(percentaje_spent_by_segment),self.build_table(percentaje_spent_by_segment),title
    def format_table_data(self, segment_index):
        segment_source = self.source_text[int(segment_index)]
        segment_modified =  self.target_text[int(segment_index)]
        id_source = int(segment_index)
        id_target = id_source + 100000
        final_output = '<a href='+ '"' + "javascript:showhide('" +str(id_source)+ "')" + '"' + '><input type="button" value="Source"></a>'
        final_output += '<a href='+ '"' + "javascript:showhide('" +str(id_target)+ "')" + '"' + '><input type="button" value="Target"></a>'
        final_output += '<div id="%d" style="display: none;height:200px;width:400px;border:1px solid #ccc;font:16px/26px Georgia, Garamond, Serif;overflow:auto;">%s</div>' % (id_source,segment_source)
        final_output += '<div id="%d" style="display: none;height:200px;width:400px;border:1px solid #ccc;font:16px/26px Georgia, Garamond, Serif;overflow:auto;">%s</div>' % (id_target,segment_modified)
        return final_output
    def build_table(self, percentaje_spent_by_segment):
        table_data_list = []
        for segment_index in percentaje_spent_by_segment:
            print segment_index
            string = "<tr><td>"+str(segment_index)
            string += self.format_table_data(segment_index)+"</td>"
            string += "<td>"+str(percentaje_spent_by_segment[segment_index])+"</td></tr>"
            table_data_list.append(string)
        return ''.join(table_data_list)
    def build_pie_as_json_string(self, percentaje_spent_by_segment):
        pie_as_json_string_list = []
        for a in percentaje_spent_by_segment:
            string = '{label: "' + str(a) + '", data: ' + str(percentaje_spent_by_segment[a]) + '}'
            pie_as_json_string_list.append(string)
        return ','.join(pie_as_json_string_list)

    def calculate_statistics_event(self, button, statistics_name):
        self.tables["translation_table"].statistics_button.hide()
        if statistics_name == "statistics_in_general":
            self.show_the_available_stats(False)
        else:
            self.calculate_statistics(statistics_name)
            self.notebook.set_current_page(6)
    def calculate_statistics(self, statistics_name):
        pie_as_json_string = ""
        if statistics_name == "time_per_segment":
            pie_as_json_string,table_data,title = self.calculate_time_per_segment()
        elif statistics_name == "insertions":
            pie_as_json_string,table_data,title = self.calculate_insertions_per_segment()
        elif statistics_name == "deletions":
            pie_as_json_string,table_data,title = self.calculate_deletions_per_segment()
        if pie_as_json_string:
            html_injector.inject_into_html(pie_as_json_string, table_data, title, statistics_name)
            self.add_statistics(statistics_name)

    def add_statistics(self, statistic_to_show):
        uri = "statistics/generated/" + statistic_to_show + '.html'
        uri = os.path.realpath(uri)
        uri = urlparse.ParseResult('file', '', uri, '', '', '')
        uri = urlparse.urlunparse(uri)
        is_linux = os.name == 'posix'
        is_windows = os.name == 'nt'
        if is_linux:
            try:
                self.notebook.remove_page(6)
                html = "<h1>This is HTML content</h1><p>I am displaying this in python</p"
                view = WebKit.WebView()
                view.open(html)
                view.load_uri(uri)
                childWidget = view
                self.notebook.insert_page(childWidget, Gtk.Label('Statistics'), 6)
                self.update_notebook()
            except:
                webbrowser.open(uri,new=2)
        if is_windows:
            webbrowser.open(uri,new=2)
