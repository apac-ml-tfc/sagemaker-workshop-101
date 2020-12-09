# Getting Started with Amazon SageMaker

This repository accompanies a hands-on training event to introduce data scientists (and ML-ready developers / technical leaders) to core model training and deployment workflows with [Amazon SageMaker](https://aws.amazon.com/sagemaker/).

## Agenda

* [00 Getting Started](00-getting-started):  Get started using the lab environment through event engine.
* [01 demo: Builtin algorithm, HPO, Tabular](00-demo-builtin_algorithm_hpo_tabular): Demonstrating how to use (and tune the hyperparameters of) a **pre-built, SageMaker-provided algorithm** (Applying XGBoost to tabular data)
* [02 lab:  Tensorflow, Keras, NLP](01-lab-custom_tensorflow_keras_nlp): Demonstrating how to **bring your own algorithm**, using SageMaker's TensorFlow container environment as a base (Classifying news headline text)
* [03 lab:  AutoPilot, Customer Churn](02-lab-auto_pilot_customer_churn): Demonstrating how to **use SageMaker Autopilot** model selection
* (Optional) [04 lab: migration_challenge_keras_image](migration_challenge_keras_image): A challenge to use what you've learned to **migrate an existing notebook** to SageMaker model training job and real-time inference endpoint deployment (Classifying MNIST DIGITS images)
