from metaflow import FlowSpec, step, IncludeFile, Parameter
import rasa


class RasaFlow(FlowSpec):
    @step
    def start(self):
        args = ''
        test.run_nlu_test(args)
        self.next(self.end)

    @step
    def end(self):
        print("hackerman")

RasaFlow()
