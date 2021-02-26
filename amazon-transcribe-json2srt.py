#convert Transcribe to srt
def process(items, between_words):
    i=1
    output=''
    isStart=False
    isEnd=False
    start_time=0
    end_time=0
    msg=''
    for index, item in enumerate(items):

        if (not item.has_key('start_time')):
            msg=msg+item['alternatives'][0]['content']
        else:
            end_time=float(item['end_time'])

        if (end_time-start_time>4.0 or index+1==len(items)):
            isEnd=True

        if (not isStart and item.has_key('start_time')):
            isStart=True
            start_time=float(item['start_time'])
            msg=msg+item['alternatives'][0]['content']
            output=output+str(i)+'\n'
            continue
            
        if (isStart and not isEnd and item.has_key('start_time')):
            msg=msg+between_words+item['alternatives'][0]['content']

        if (isStart and isEnd):
            hour=int(start_time/60/60)
            min=int(start_time/60)-hour*60
            sec=int(start_time)-min*60-hour*60*60
            msec=int((start_time-sec)*1000)  
            e_hour=int(end_time/60/60)
            e_min=int(end_time/60)-e_hour*60
            e_sec=int(end_time)-e_min*60-e_hour*60*60
            e_msec=int((end_time-sec)*1000)
            msg1='{}:{}:{},{} --> {}:{}:{},{}'.format(hour,min,sec,msec, e_hour,e_min,e_sec,e_msec)+'\n'
            output=output+msg1+msg+between_words+item['alternatives'][0]['content']+'\n\n'
            i=i+1
            isStart=False
            isEnd=False
            start_time=end_time
            msg=''
    return output

def main():
    import sys
    import json
    import datetime
    import codecs
    import argparse

    parser = argparse.ArgumentParser(description='convert Amazon Transcribe JSON file to SRT subtitle file.')
    parser.add_argument("--space", action="store_true", 
                    help="space between words")
    parser.add_argument("JSONFILE",
                    help="Amazon Transcribe JSON file")
    args = parser.parse_args()

    filename=args.JSONFILE

    if (args.space):
        between_words=" "
    else:
        between_words=""

    print ("Input Filename: ", filename)
    print ("Onput Filename: ", filename+'.srt')

    with codecs.open(filename+'.srt', 'w', 'utf-8') as w:
        with codecs.open(filename, 'r', 'utf-8') as f:
            data=json.loads(f.read())
            output=process(data["results"]['items'], between_words)
            w.write(output)

if __name__ == '__main__':
    main()
