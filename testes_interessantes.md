rasa run -m models/ -v --endpoints endpoints/endpoints.yml --credentials credentials/credentials.yml

# Executando o teste via código em python

```python
from argparse import Namespace
from rasa.cli.test import run_core_test
args = Namespace(
        config=None,
        cross_validation=False,
        stories='.',
        endpoints='endpoints.yml',
        out='results/',
        no_errors=False,
        no_warnings=False,
        model='models',
        nlu='data',
        evaluate_model_directory=False,
        fail_on_prediction_errors=False,
        percentages=[0,
        25,
        50,
        75],
        max_stories=None,
        runs=3,
        e2e=True,
        successes=False,
        warnings=True
)
test.run_core_test(args)
test.run_nlu_test(args)
```