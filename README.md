# Medical assistant for question answering

Scenario: You are working for a medical certification board exploring the use of short-answer questions for continuing certification exams. You are asked to build a prototype grading model that can automatically score short, free-text responses (1-3 sentences) given a reference “ideal” answer.
Objective: Please share and explain your approach to reach the goal.

## How to run
To run the Automated Grading Prototype, download the code from the GitHub repo, ensure you have all required Python packages installed (e.g., streamlit, sentence-transformers, scikit-learn, etc.), and then simply execute the included Bash script. To do this, open a terminal, navigate to the project directory, and run ./prototype_runner.sh. This script launches the prototype_app.py Streamlit application, which provides a web interface for grading short free-text answers using sentence embeddings and similarity metrics. Make sure the script has execute permissions (chmod +x prototype_runner.sh) before running it. Once you run the application, there may be a few seconds of delay until the application is completely rendered. In this, you will see on the top right corner, a sign, that reads "RUNNING". Please wait until the application fully rendered.

## Approach


## Transformer models


## Example output

## File structure
<pre><code>
grading_model/ 


</code></pre>

## List of demo functionalities


## Limitations and future work

## Citations:

### Embedding transformer models
BioBERT: https://huggingface.co/pritamdeka/BioBERT-mnli-snli-scinli-scitail-mednli-stsb<br>
PubMedBERT: https://huggingface.co/pritamdeka/S-PubMedBert-MS-MARCO<br>
MiniLM-L6: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2<br>
MiniLM-L12: https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2<br>
paraphrase-MiniLM-L6: https://huggingface.co/sentence-transformers/paraphrase-MiniLM-L6-v2
