from traceloop.sdk import Traceloop
from traceloop.sdk.decorators import workflow
from transformers import pipeline

Traceloop.init(disable_batch=True)

@workflow(name="analyse")
def analyse(statement):
    classifier = pipeline("sentiment-analysis")
    res=classifier(statement)
    print(res)

    
analyse("I am Happy to be here at Karunya University.Very Beautiful place..")
