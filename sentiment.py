from traceloop.sdk import Traceloop
from traceloop.sdk.decorators import workflow
from transformers import pipeline

Traceloop.init(disable_batch=True)

@workflow(name="analyse")
def analyse(statement):
    classifier = pipeline("sentiment-analysis")
    res=classifier(statement)
    print(res)

    
analyse("I have been waiting for a hugging face course my whole life.")
root@borak1:~/n# cat /root/karunya/
cat: /root/karunya/: Is a directory
root@borak1:~/n# ls /root/karunya/
'='   apikey.sh   medquad_qa_pairs.csv   py_vectordb_trace.py   sentiment.py   traceloop_env.sh
root@borak1:~/n# cat /root/karunya/sentiment.py 
from traceloop.sdk import Traceloop
from traceloop.sdk.decorators import workflow
from transformers import pipeline

Traceloop.init(disable_batch=True)

@workflow(name="analyse")
def analyse(statement):
    classifier = pipeline("sentiment-analysis")
    res=classifier(statement)
    print(res)
