import os
import json
import difflib

class Differences:

    def __init__(self, original_target_path):
        self.saved_original_file = original_target_path

    def add_colored_differences(self, original_segment, modified_segment, color = "green"):
        offset = 0
        array_to_use = []
        insertions,deletions = self.get_insertion_and_deletions(original_segment, modified_segment)

        array_to_use = deletions;
        segment_to_use = original_segment
        nice_color = "#F8CBCB"
        if color == "green":
            array_to_use = insertions
            segment_to_use = modified_segment
            nice_color = "#A6F3A6"

        for tuple in array_to_use:
            start = tuple[0] + offset
            end = tuple[1] + offset
            print start,end
            enrichedText = "<span style=\"background-color: " + nice_color + "; font-weight:600;\" >"
            enrichedText += segment_to_use[start:end]
            enrichedText += "</span>"
            segment_to_use = segment_to_use[:start] + enrichedText + segment_to_use[end:]
            offset += len(enrichedText) - (end - start)
        if "span" in segment_to_use: print segment_to_use
        return segment_to_use

    def get_insertion_and_deletions(self, original_segment, modified_segment):
        s = difflib.SequenceMatcher(None, original_segment, modified_segment)
        insertions = []
        deletions = []
        for tag, i1, i2, j1, j2 in s.get_opcodes():
            if tag == "insert" or tag == "replace":insertions.append((j1,j2))
            if tag == "delete"or tag == "replace": deletions.append((i1,i2))
        return (insertions,deletions)

    def load_log(self):
        log = {}
        log_filepath = os.path.abspath("./saved/" + "log.json")
        try:
            with open(log_filepath) as json_data:
                log = json.load(json_data)
        except:pass
        return log

    def get_latest_modifications (self):
        log = self.load_log()
        last_modifications = {}
        for a in sorted(log.keys()):
            for b in log[a]:
                last_modifications[b] = log[a][b]
        return last_modifications

    def get_modified_and_unmodified_target(self):
        self.unmodified_target = []
        self.modified_target = []
        with open(self.saved_original_file) as fp:
            for line in fp:
                if line != '\n':
                    self.unmodified_target.append(line)
        latest_modifications = self.get_latest_modifications()
        for index, line in enumerate(self.unmodified_target):
            if str(index) in latest_modifications:
                self.modified_target.append(latest_modifications[str(index)])
            else:
                self.modified_target.append(line)
        return self.modified_target, self.unmodified_target

    def get_enriched_text(self):
        enriched_texts_segments_original = []
        enriched_texts_segments_modified = []
        self.get_modified_and_unmodified_target()
        for unmod, mod in zip(self.unmodified_target, self.modified_target):
            enriched_texts_segments_original.append(self.add_colored_differences(unmod,mod,"red"))
            enriched_texts_segments_modified.append(self.add_colored_differences(unmod,mod,"green"))
        return enriched_texts_segments_original, enriched_texts_segments_modified
