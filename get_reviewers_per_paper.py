from openreview import *
#client = openreview.Client(
openreview = Client(baseurl="https://openreview.net", username="iclr2018admin", password="sainath")
import os

# This script outputs the number of ACs assigned to all papers listed in id_title_list.txt

# Get papers
f = open('id_title_list.txt', 'w')
for paper_id in range(1,1000):
  try:
    notes = openreview.get_notes(invitation = 'ICLR.cc/2018/Conference/-/Submission', number = paper_id)
    if len(notes) > 0:
        note = notes[0]
        reviewers = openreview.get_group('ICLR.cc/2018/Conference/Paper' + str(note.number) + '/Reviewers');
        n_reviewers = ""
        for rev in reviewers.members:
            n_reviewers = n_reviewers + rev.encode('utf-8') + ","
            #reviewer_wrapper=openreview.get_group(rev)

            #if len(reviewer_wrapper.members) > 0:
            #    n_reviewers = n_reviewers + 1
#            else:
#                print "Reviewer group has no members", reviewer_wrapper.id, "for paper", paper_id
        line = str(paper_id) + "," + n_reviewers
        print line
        f.write(line+'\n')
  except Exception:
      pass
      print "Paper",paper_id,"not found"

f.close()
