# Getting Started with Amazon SageMaker

This repository accompanies a hands-on training event to introduce data scientists (and ML-ready developers / technical leaders) to core model training and deployment workflows with [Amazon SageMaker](https://aws.amazon.com/sagemaker/).

## Agenda

* [00 demo: builtin_algorithm_hpo_tabular](00-demo-builtin_algorithm_hpo_tabular): Demonstrating how to use (and tune the hyperparameters of) a **pre-built, SageMaker-provided algorithm** (Applying XGBoost to tabular data)
* [01 lab:  custom_tensorflow_keras_nlp](01-lab-custom_tensorflow_keras_nlp): Demonstrating how to **bring your own algorithm**, using SageMaker's TensorFlow container environment as a base (Classifying news headline text)
* [02 lab:  02-lab-auto_pilot_customer_churn](02-lab-auto_pilot_customer_churn): Demonstrating how to **use SageMaker Autopilot** model selection
* (Optional) [03 lab: migration_challenge_keras_image](migration_challenge_keras_image): A challenge to use what you've learned to **migrate an existing notebook** to SageMaker model training job and real-time inference endpoint deployment (Classifying MNIST DIGITS images)


## Setup

1. Clone the repository into the Studio Environment
    - Select the GitHub icon in the panel on the left and click "Clone Repository". Enter `https://github.com/tom5610/sagemaker-workshop-101.git`.
    - Alternatively launch a **System terminal** (from the *Other* section of the launcher screen) and run `git clone https://github.com/tom5610/sagemaker-workshop-101.git`.

2. Enable Extension Manager
    - Select \"*Settings > Enable Extension Manager (experimental)*\" from the toolbar, and confirm to enable it
    - Click on the new jigsaw puzzle piece icon in the sidebar on the left, to open the Extension Manager
    - Search for `@jupyter-widgets/jupyterlab-manager` (Scroll down - search results show up *below* the list of currently installed widgets!)
    - Click \"**Install**\" below the widget's description, if not installed already
    - Wait for the blue progress bar that appears by the search box
    - You should be prompted \"*A build is needed to include the latest changes*\" - select \"**Rebuild**\"
    - The progress bar should resume, and you should shortly see a \"Build Complete\" dialogue.
    - Select \"**Reload**\" to reload the webpage

3. You'll be asked to select a kernel when you first open each notebook. Use **Python 3 (Data Science)** as standard and **Python 3 (TensorFlow CPU Optimized)** for the 'local' notebooks in NLP and migration challenge folders - they will TensorFlow models within the notebook itself.

You can refer to the [*"How Are Amazon SageMaker Studio Notebooks Different from Notebook Instances?"*](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-comparison.html) docs page for more details on differences between the Studio and Notebook Instance environments.
