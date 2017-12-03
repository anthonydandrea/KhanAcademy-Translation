import csv
import codecs

def parse(f):
    fStrings = []
    for line in f:
        fStrings.append(line)
    with open('SwedishWordData.csv','w',newline='') as csvfile:
        fieldnames = ['word','part_of_speech']
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        for inx in range(len(fStrings)):
            if '<lemma-entry>' in fStrings[inx]:
                writer.writerow({'word': fStrings[inx+1][7:fStrings[inx+1].index('</form>')].replace('~','-'), 'part_of_speech': fStrings[inx+4][6:fStrings[inx+4].index('</')-1]})
                #writer.writerow({'word': fStrings[inx+1][7:fStrings[inx+1].index('</form>')], 
                                #'part_of_speech': fStrings[inx+4]})



if __name__ == '__main__':
    f = codecs.open('LEXIN.xml','r',encoding='iso-8859-1',errors='ignore')
    parse(f)


    
