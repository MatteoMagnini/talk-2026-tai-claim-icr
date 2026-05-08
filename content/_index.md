+++

title = "SKE & SKI: Theory and Methods"
description = "Symbolic Knowledge Extraction and Injection: Theory and Methods"
outputs = ["Reveal"]

+++

{{% section %}}

# Symbolic Knowledge Extraction and Injection:<br>Theory and Methods

<span class="hint">(last built on: {{< today >}})</span>

{{< mm >}}
<br> Department of Computer Science and Engineering (DISI)
<br> Alma Mater Studiorum—University of Bologna

<br>ICR-CLAiM Seminar @ [DCS, FSTM, University of Luxembourg](https://www.uni.lu/fstm-en/research-departments/department-of-computer-science/)
<br>4th November 2025, Esch-sur-Alzette, Luxembourg

<br>

---

## Link to these slides

<{{< slides-url >}}>

{{< qrcode >}}

[<i class="fa fa-print" aria-hidden="true"></i> printable version](?print-pdf&pdfSeparateFragments=false)

{{% /section %}}

---

{{% section %}}

{{< slide id="about me" >}}

# About me

{{% multicol %}}

{{% col %}}

{{< image src="./images/matteo.jpeg" alt="Matteo Magnini" width="100%" max-h="50vh" >}}

{{% /col %}}

{{% col %}}

## Research topics

- <span style="font-size: smaller;">Symbolic and Neuro-Symbolic AI (NeSy)</span>
  - Symbolic Knowledge Injection (SKI)
  - Symbolic Knowledge Extraction (SKE)
- <span style="font-size: smaller;">Explainable AI (XAI)</span>
- <span style="font-size: smaller;">Fairness in AI</span>
  - Regularization for Group Fairness
- <span style="font-size: smaller;">Large Language Models (LLMs)</span>
  - RAG pipelines
  - Medical applications

{{% /col %}}

{{% col %}}

## Interests

- <span style="font-size: smaller;">Scuba Diver</span>
  - NADD ADV
  - ~40 dives
- <span style="font-size: smaller;">Chess</span>
  - ELO ~1750 (estimated)
- <span style="font-size: smaller;">History</span>
- <span style="font-size: smaller;">Hiking</span>
- <span style="font-size: smaller;">Cooking</span>
  - (or should I say eating)

{{% /col %}}

{{% /multicol %}}

---

{{% multicol %}}

# Recent updates

{{% col %}}

{{% /col %}}

{{% col %}}

{{< image src="./images/wedding.jpg" alt="Wedding" width="100%" max-h="70vh" >}}

{{% /col %}}

{{% col %}}

{{< image src="./images/frontispiece.png" alt="Wedding" width="100%" max-h="70vh" >}}

{{% /col %}}

{{% col %}}

{{% /col %}}

{{% /multicol %}}

{{% /section %}}

---

{{< slide id="background" >}}

# Background

Quick overview on symbolic vs. sub-symbolic AI

---

{{% section %}}

## Overview on AI

{{< image src="./images/ai-map.svg" alt="AI map" width="100%" >}}

- wide field of research, with many _sub-fields_
- each sub-field has its own relevant _tasks_ (problems) ...
- ... and each task comes with many useful _methods_ (algorithms)

---

## Symbolic vs. Sub-symbolic AI

Two broad categories of AI approaches:

{{< image src="./images/ai-map2.svg" alt="AI map with a focus on symbolic vs sub-symbolic" width="100%" >}}

{{% /section %}}

---

{{% section %}}

## Why the wording "Symbolic" vs. "Sub-symbolic"? (pt. 1)

### Local vs. Distributed Representations

{{% multicol %}}
{{% col %}}
{{< image src="./images/local-distributed-representations.png" alt="Local vs. Distributed Representations of a bunch of animals" width="100%" max-h="60vh" >}}
{{% /col %}}
{{% col %}}
<br>

- __Local__ $\approx$ "symbolic": each symbol has a clear, distinct meaning
    + e.g. `"bear"` is a symbol denoting a crisp category (either the animal is a bear or not)

- __Distributed__ $\approx$ "non-symbolic": symbols do not have a clear meaning per se, but the whole representation does
    + e.g. `"swim"` is fuzzy capability: one animal may be (un)able to swim to some extent

<br>

{{% fragment %}}
> Let's say we need to represent $N$ classes, how many columns would the tables have?
> {{% /fragment %}}

{{% /col %}}
{{% /multicol %}}

---

## Why the wording "Symbolic" vs. "Sub-symbolic"? (pt. 2)

### What is a "symbol" after all? Aren't numbers symbols too?

According to [Tim van Gelder in 1990](https://doi.org/10.1007/978-3-642-76070-9_6):

> __Symbolic__ representations of knowledge
> - involve a _set of symbols_
> - which can be _combined_ (e.g., concatenated) in (possibly) infinitely many ways,
> - following precise _syntactical rules_,
> - where both elementary symbols and any admissible combination of them can be _assigned with meaning_

---

## Why "*Sub*-symbolic" instead of "Non-symbolic" or just "Numerical"?

- There exist approaches where symbols are combined with numbers, e.g.:
    + **Probabilistic logic programming**: where logic statements are combined with probabilities
    + **Fuzzy logic**: where logic statements are combined with degrees of truth
    + **Bayesian networks**: a.k.a. graphical models, where nodes are symbols and edges are conditional dependencies with probabilities, e.g.
        ![Example of a Bayesian network](./images/bn.png)

- These approaches are _not purely symbolic_, but they are _not purely numeric_ either, so we call the overall category __"sub-symbolic"__

{{% /section %}}

---

{{% section %}}

## Examples of Symbolic AI (pt. 1)

- **Logic programming**: SLD resolution (e.g., Prolog)
- **Knowledge representation**: Semantic Web (e.g., OWL), Description Logics (e.g., ALC)
- **Automated reasoning**: Theorem proving, Model checking
- **Planning**: STRIPS, PDDL

---

## Examples of Symbolic AI (pt. 2)

### Logic programming with SLD resolution

{{< image src="./images/proof-tree.png" alt="Example of SLD resolution on a simple theory" width="100%" max-h="60vh" >}}

---

## Examples of Symbolic AI (pt. 3)

### Ontology definition in OWL

{{< image src="./images/ontology-example.png" alt="Example of ontology definition in OWL" width="80%" max-h="60vh" >}}

---

## Examples of Symbolic AI (pt. 4)

### Model-checking (as opposed to testing)

{{< image src="./images/model-checking-vs-testing.webp" alt="Main differences among model-checking and testing for verifying computational systems" width="80%" max-h="60vh" >}}

---

## Examples of Symbolic AI (pt. 5)

### Planning in STRIPS

{{% multicol %}}
{{% col %}}
{{< image src="./images/planning.png" alt="Example of start vs goal state + state branching" width="100%" max-h="60vh" >}}
{{% /col %}}
{{% col %}}

<br>

#### Available actions

- `grab(X)`: grabs block `X` from the table
- `put(X)`: puts block `X` on the table
- `stack(X, Y)`: stacks block `X` on top of block `Y`
- `unstack(X, Y)`: un-stacks block `X` from block `Y`

{{% /col %}}
{{% /multicol %}}

{{% /section %}}

---

## What do these _symbolic_ approaches have in common?

- **Structured representations**: knowledge (I/O data) is represented in a structured, formal way (e.g., logic formulas, ontologies)

- **Algorithmic manipulation of representations**: each approach relies on algorithms that manipulate these structured representations following exact rules

- **Crisp semantics**: the meaning of the representations is well-defined, and the algorithms produce exact results
    + representations are either _well-formed or not_, algorithms rely on rules which are either _applicable or not_

- **Model-driven**: algorithms may commonly work in zero- or few-shot settings, humans must commonly model and encode knowledge in the target structure

- **Clear computational complexity**: the decidability, complexity, and tractability of the algorithms are well understood

---

{{% section %}}

## Examples of Sub-symbolic AI (pt. 1)

- **Machine learning**: supervised, unsupervised, and reinforcement learning
    * _Supervised_ learning: fitting a discrete (classification) or a continuous function (regression) from examples
    * _Unsupervised_ learning: clustering, dimensionality reduction
    * _Reinforcement_ learning: learning a policy to maximize a reward signal, via simulation

- **Probabilistic reasoning**: Bayesian networks, Markov models, probabilistic logic programming

---

## Examples of Sub-symbolic AI (pt. 2)

### Supervised learning

{{< image src="./images/supervised.png" alt="Overview on the supervised learning process" width="100%" max-h="60vh" >}}

---

## Examples of Sub-symbolic AI (pt. 3)

### Supervised learning – Classification vs. Regression (1/2)

Data separation vs. curve fitting:

{{< image src="./images/classification-vs-regression1.png" alt="Classification vs. Regression: separation vs. curve fitting" width="100%" max-h="60vh" >}}

---

## Examples of Sub-symbolic AI (pt. 4)

### Supervised learning – Classification vs. Regression (2/2)

Focus on the target feature:

{{< image src="./images/classification-vs-regression2.png" alt="Classification vs. Regression: finite vs. continuous target feature" width="100%" max-h="60vh" >}}

---

## Examples of Sub-symbolic AI (pt. 5)

### Unsupervised learning – Clustering

{{< image src="./images/clustering.png" alt="Example of the clustering task" width="100%" max-h="60vh" >}}

---

## Examples of Sub-symbolic AI (pt. 6)

### Unsupervised learning – Reinforcement learning (metaphor)

{{< image src="./images/reinforcement.svg" alt="Main idea behind reinforcement learning" width="100%" max-h="60vh" >}}

---

## Examples of Sub-symbolic AI (pt. 7)

### Reinforcement learning – Reinforcement learning (policy)

{{< image src="./images/q-table.png" alt="The goal of reinforcement learning is to estimate a policy, i.e. a function (e.g. a table) estimating the expected reward per each state–action pair" width="100%" max-h="60vh" >}}

{{% /section %}}

---

## What do these _sub-symbolic_ approaches have in common?

- **Numeric representations**: knowledge (I/O data) is represented in a less structured way, often as vectors/matrices/tensors of numbers

- **Differentiable manipulation of representations**: algorithms rely on mathematical operations involving these numeric representations, most-commonly undergoing some optimization process
    + e.g., sum, product, max, min, etc.

- **Fuzzy/continuous semantics**: representations are from continuous spaces, where similarities and distances are defined in a continuous way, and algorithms may yield fuzzy results

- **Data-driven** + **Usage vs. training**: algorithms are often trained on data, to be later re-used on other data
    + usage is commonly impractical or impossible without training

- **Unclear computational complexity**: strong reliance on greedy or time-limited optimization methods, lack of theoretical guarantees on the quality of the results

---


## Long-standing dualism

### Intuition vs. Reasoning

1. Esprit de _finesse_ vs. Esprit de _géométrie_ (Philosophy) --- [Blaise Pascal, 1669](https://en.wikipedia.org/wiki/Pens%C3%A9es)
2. _Cognitive_ vs. _Behavioural_ Psychology --- [B.F. Skinner, 1950s](https://doi.org/10.1111/j.2044-8295.1985.tb01953.x)
3. _System 1_ (fast, intuitive) vs. _System 2_ (slow, rational) --- [Daniel Kahneman, 2011](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow)

##

{{% fragment %}}
{{% multicol %}}
{{% col %}}
#### Sub-symbolic AI

- Provides mechanisms emulating human-like _intuition_
- _Quick_, possibly _error-prone_, but often _effective_
- Requires _learning_ from data
- Often _opaque_, hard to interpret or explain
{{% /col %}}
{{% col %}}
#### Symbolic AI

- Provides mechanisms emulating human-like _reasoning_
- _Slow_, but _precise_ and _verifiable_
- Requires symbolic _modeling_ and _encoding_ knowledge
- Often _transparent_, easier to interpret and explain
{{% /col %}}
{{% /multicol %}}
{{% /fragment %}}

---

## Need for integration

- the [NeSy community](https://www.nesy-ai.org/) has long recognized the _complementarity_ among symbolic and sub-symbolic approaches...
- ... with a focus on __neural-networks__ (_NN_) based sub-symbolic methods, as they are very _flexible_

{{% fragment %}}

### Patterns of _integration_ or _combination_ (cf. [Bhuyan et al., 2024](https://link.springer.com/article/10.1007/s00521-024-09960-z))

1. `Symbolic Neuro-Symbolic`: symbols $\rightarrow$ vectors $\rightarrow$ NNs $\rightarrow$ vectors $\rightarrow$ symbols
2. `Symbolic[Neuro]`: symbolic module $\xrightarrow{invokes}$ NN $\rightarrow $ output
3. `Neuro | Symbolic`: NN $\xrightarrow{cooperates}$ symbolic module $\xrightarrow{cooperates}$ NN $\rightarrow$ ...
4. `Neuro-Symbolic → Neuro`: symbolic knowledge $\xrightarrow{influences}$ NN
5. <code>Neuro<sub>Symbolic</sub></code>: symbolic knowledge $\xrightarrow{constrains}$ NN
6. `Neuro[Symbolic]`: symbolic module $\xrightarrow{\textit{embedded in}}$ NN

{{% /fragment %}}

---

## Focus on two main approaches

(cf. [Ciatto et al., 2024](https://doi.org/10.1145/3645103))

- Symbolic Knowledge **Extraction** (_SKE_): extracting symbolic knowledge from sub-symbolic models
    * for the sake of _explainability_ and _interpretability_ in machine learning

- Symbolic Knowledge **Injection** (_SKI_): injecting symbolic knowledge into sub-symbolic models
    * for the sake of _trustworthiness_ and _robustness_ in machine learning

{{% fragment %}}
Both require some basic understanding of how _supervised_ __machine learning__ works
{{% /fragment %}}

---

{{< slide id="ske" >}}

# Symbolic Knowledge Extraction (SKE)

How to extract symbolic knowledge from sub-symbolic predictors

---

{{% section %}}

## Definition and Motivation (pt. 1)

> any _algorithmic procedure_ accepting trained sub-symbolic predictors as input and producing _symbolic_ knowledge as output, so that the extracted knowledge reflects the behaviour of the predictor with high _fidelity_.

---

## Definition and Motivation (pt. 2)

- **Explainable AI (XAI)**: SKE methods are often used to provide explanations for the decisions made by sub-symbolic predictors, making them more interpretable and understandable to humans (a.k.a. _post-hoc explainability_)
  - _local explanations_: explanations for individual predictions
  - _global explanations_: explanations for the overall behaviour of the predictor

- **Knowledge discovery**: SKE methods can help discover patterns and relationships in the data that may not be immediately apparent, thus providing insights into the underlying processes

- **Model compression**: SKE methods can simplify complex sub-symbolic models by extracting symbolic rules that approximate their behaviour, thus reducing the model's size and complexity

---


## Explainability vs Interpretability

They are _not_ synonyms in spite of the fact that they are often used interchangeably!

{{% multicol %}}

{{% col %}}

<h3 style="text-align: center; color: blue">
Explanation
</h3>

- elicits _relevant aspects_ of objects (to ease their interpretation)

- it is an operation that transform poorly interpretable objects into _more interpretable_ ones

- search of a _surrogate_ interpretable model

{{% /col %}}

{{% col %}}

<h3 style="text-align: center; color: blue">
Interpretation
</h3>

- binds objects with _meaning_ (what the human mind does)

- it is _subjective_

- it does not need to be measurable, only _comparisons_

{{% /col %}}

{{% /multicol %}}

---

## Concepts

Main entities and how to extract symbolic knowledge from sub-symbolic predictors

---

## Entities

{{% multicol %}}

{{% col %}}

<h3 style="text-align: center; color: blue">
Sub-symbolic predictor
</h3>

{{< image src="./images/nn-iris.png" alt="Example of a neural network trained on the Iris dataset" width="100%" max-h="60vh" >}}

{{% /col %}}

{{% col %}}

<h3 style="text-align: center; color: blue">
Symbolic knowledge
</h3>

<div style="margin-top: 10vh; margin-left: 5vw;">


| Logic Rule                                                                                                   |
|--------------------------------------------------------------------------------------------------------------|
| Class = setosa ← PetalWidth ≤ 1.0                                                                            |
| Class = versicolor ← PetalLength > 4.9 ∧ <br><div style="margin-left: 15vw;"> SepalWidth ∈ [2.9, 3.2] </div> |
| Class = versicolor ← PetalWidth > 1.6                                                                        |
| Class = virginica ← SepalWidth ≤ 2.9                                                                         |
| Class = virginica ← SepalLength ∈ [5.4, 6.3]                                                                 |
| Class = virginica ← PetalWidth ∈ [1.0, 1.6]                                                                  |

</div>

{{% /col %}}

{{% /multicol %}}

---

## How SKE works

{{% multicol %}}

{{% col %}}

<h3 style="text-align: center; color: blue">
Decompositional SKE
</h3>

> if the method _needs_ to inspect (even partially) the internal parameters of the underlying black-box predictor, e.g., neuron biases or connection weights for NNs, or support vectors for SVMs

{{% /col %}}

{{% col %}}

<h3 style="text-align: center; color: blue">
Pedagogical SKE
</h3>

> if the algorithm _does not need_ to take into account any internal parameter, but it can extract symbolic knowledge by only relying on the predictor’s outputs.

{{% /col %}}

{{% /multicol %}}

{{% /section %}}

---

{{% section %}}

## CART (pt. 1)
Classification and regression trees (cf. [Breiman et al., 1984](https://doi.org/10.1201/9781315139470))

{{< image src="./images/dt-kyphosis.png" alt="Example of a decision tree" width="80%" max-h="60vh" >}}

An example decision tree estimating the probability of kyphosis after spinal surgery, given the _age_ of the patient and the vertebra at which surgery was _start_ ed (rf. [wiki:dt-learning](https://en.wikipedia.org/w/index.php?title=Decision_tree_learning)).
Notice that all decision trees subtend a partition of the input space, and that those trees themselves provide intelligible representations of _how_ predictions are attained.

---

## CART (pt. 2)

1. generate a _synthetic_ dataset by using the predictions of the sub-symbolic predictor

2. _train_ a decision tree on the synthetic dataset

3. compute the _fidelity_ and repeat step 2 until satisfied

4. [optional] rewrite the tree as a set of symbolic _rules_

---

## Adult classification task (pt. 1)

The Adult dataset (cf. [Becker Barry and Kohavi Ronny, 1996](https://doi.org/10.24432/C5XW20)) contains the records (48,842) of individuals based on census data (this dataset is also known as Census Income).
The dataset has many features (14) related to the individuals' demographics, such as age, education, and occupation.
The target feature is whether the individual earns more than `$50,000` per year.

<br>

<div style="text-align: center; color: blue;">Examples of Adult records</div>

<br>

| age | workclass        | education | ... | hours-per-week | native-country | income |
|-----|------------------|-----------|-----|----------------|----------------|--------|
| 39  | State-gov        | Bachelors | ... | 40             | United-States  | <=50K  |
| 50  | Self-emp-not-inc | Bachelors | ... | 13             | United-States  | <=50K  |
| 38  | Private          | HS-grad   | ... | 40             | United-States  | <=50K  |
| 53  | Private          | 11th      | ... | 40             | United-States  | <=50K  |
| 28  | Private          | Bachelors | ... | 40             | Cuba           | <=50K  |
| 37  | Private          | Masters   | ... | 40             | United-States  | <=50K  |
| 49  | Private          | 9th       | ... | 16             | Jamaica        | <=50K  |
| 52  | Self-emp-not-inc | HS-grad   | ... | 45             | United-States  | >50K   |
| 31  | Private          | Masters   | ... | 50             | United-States  | >50K   |
| 42  | Private          | Bachelors | ... | 40             | United-States  | >50K   |


---

## Adult classification task (pt. 2)

We can train a simple feed-forward neural network for a fixed amount of epoches on the Adult dataset to classify whether an individual earns more than `$50,000` per year.

{{% multicol %}}

{{% col %}}

```python
class AdultNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(FEATURE_NUMBER, HIDDEN_SIZE),
            nn.ReLU(),
            nn.Linear(HIDDEN_SIZE, HIDDEN_SIZE),
            nn.ReLU(),
            nn.Linear(HIDDEN_SIZE, CLASS_NUMBER)
        )

    def forward(self, x):
        return self.model(x)
```

{{% /col %}}

{{% col %}}


```python
def train_model() -> tuple[nn.Module, list[float]]:
    model = AdultNet()
    model.to(device)
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()
    train_losses = []
    for epoch in range(EPOCHES):
        model.train()
        optimizer.zero_grad()
        output = model(X_train_tensor)
        loss = criterion(output, y_train_tensor)
        loss.backward()
        optimizer.step()
        train_losses.append(loss.item())
        if (epoch + 1) % 10 == 0 or epoch == EPOCHES - 1:
            print(f"Epoch {epoch+1}: loss = {loss.item():.4f}")
    return model, train_losses
```

{{% /col %}}

{{% /multicol %}}

---

## Adult classification task (pt. 3)

{{% multicol %}}

{{% col %}}

{{< image src="./images/extraction_files/extraction_15_0.png" alt="Loss during training" width="100%" max-h="60vh" >}}

{{% /col %}}

{{% col %}}

<br>
<div style="text-align: center;">SciKitLearn classification report</div>
<br>

| Class        | Precision | Recall   | F1-Score | Support |
|--------------|-----------|----------|----------|---------|
| <=50K        | 0.867812  | 0.935882 | 0.900562 | 24.720  |
| >50K         | 0.731447  | 0.550568 | 0.628247 | 7.841   |
| Accuracy     |           |          | 0.843094 | 32.561  |
| Macro Avg    | 0.799629  | 0.743225 | 0.764405 | 32.561  |
| Weighted Avg | 0.834974  | 0.843094 | 0.834986 | 32.561  |

{{% /col %}}

{{% /multicol %}}

---

## Extracted rules (pt. 1)

{{% multicol %}}

{{% col %}}

{{< image src="./images/extraction_files/extraction_25_0.png" alt="Decision tree" width="100%" max-h="100vh" >}}

{{% /col %}}

{{% col %}}

{{< image src="./images/extraction_files/extracted-symbolic-rules.png" alt="Decision tree" width="100%" max-h="60vh" >}}

{{% /col %}}

{{% col %}}
<div style="font-size: 1.15rem; line-height: 1.5; font-family: 'Fira Sans', 'Helvetica Neue', sans-serif;">

**Decision Rules**

1. **class = 0** if `education ≤ 12.5` and `capital-gain ≤ 3048`
2. **class = 1** if `education ≤ 12.5` and `capital-gain > 3048`
3. **class = 0** if `education > 12.5` and `occupation ≤ 0.5` and `hours-per-week ≤ 31`
4. **class = 1** if `education > 12.5` and `occupation ≤ 0.5` and `hours-per-week > 31`
5. **class = 0** if `education > 12.5` and `occupation > 0.5` and `capital-gain ≤ 3869` and `occupation ≤ 4.5`
6. **class = 1** if `education > 12.5` and `occupation > 0.5` and `capital-gain ≤ 3869` and `occupation > 4.5`
7. **class = 1** if `education > 12.5` and `occupation > 0.5` and `capital-gain > 3869`

</div>


{{% /col %}}

{{% /multicol %}}

---

## Extracted rules (pt. 2)

<br>
<div style="text-align: center;">Fidelity of the symbolic predictor</div>
<br>

| Class        | Precision | Recall | F1-Score | Support |
|--------------|-----------|--------|----------|---------|
| 0            | 0.97      | 0.98   | 0.97     | 26659   |
| 1            | 0.89      | 0.84   | 0.86     | 5902    |
| Accuracy     |           |        | 0.95     | 32561   |
| Macro Avg    | 0.93      | 0.91   | 0.92     | 32561   |
| Weighted Avg | 0.95      | 0.95   | 0.95     | 32561   |

---

Jupyter notebook available here

[github.com/MatteoMagnini/demo-2025-woa-nesy/blob/master/notebook/extraction.ipynb](https://github.com/MatteoMagnini/demo-2025-woa-nesy/blob/master/notebook/extraction.ipynb)

{{< image src="./images/ske-notebook-qr.svg" alt="QR code to the Jupyter notebook" width="20%" >}}


{{% /section %}}

---

{{% section %}}

## Taxonomy of SKE methods (pt. 1)

{{< image src="./images/ske-taxonomy.svg" alt="Taxonomy of SKE methods" width="80%" >}}

---

## Taxonomy of SKE methods (pt. 2)

{{% multicol %}}

{{% col %}}

<div style="text-align: center;">
<h3 style="color: blue">
Target AI task
</h3>

- _classification_<br> $f: 𝒳 ⊆ ℝⁿ → 𝒴 s.t. |𝒴| = k$

- _regression_<br> $f: 𝒳 ⊆ ℝⁿ → 𝒴 ⊆ ℝᵐ$
</div>

{{% /col %}}

{{% col %}}

<div style="text-align: center;">
<h3 style="color: blue">
Input data
</h3>

- _binary_<br> $𝒳 ≡ {0, 1}ⁿ$

- _discrete_<br> $𝒳 ∈ {x₁, ..., xₙ}ⁿ$

- _continuous_<br> $𝒳 ⊆ ℝⁿ$
</div>

{{% /col %}}

{{% /multicol %}}

---

## Taxonomy of SKE methods (pt. 3)

{{% multicol %}}

{{% col %}}

<h3 style="text-align: center; color: blue">
Shape
</h3>

- _rule list_, ordered sequences of if-then-else rules

- _decision tree_, hierarchical set of if-then-else rules involving a comparison among a variable and a constant

- _decision table_, 2D tables summarising decisions for each possible assignment of the input variables

{{% /col %}}

{{% col %}}

<h3 style="text-align: center; color: blue">
Expressiveness
</h3>

- _propositional_, boolean statements + logic connectives, including arithmetic comparisons among variables and constants

- _fuzzy_, hierarchical set of if-then-else rules involving a comparison among a variable and a constant

- _oblique_, boolean statements + logic connectives + arithmetic comparisons

- _M-of-N_, any of the above + statements of the form "at least $k$ of the following statements are true"

{{% /col %}}

{{% /multicol %}}

---

## Discussion

{{% multicol %}}

{{% col %}}

### **Notable remarks**

- discretisation of the input space

- discretisation of the output space

- features should have semantic meaning

- rules constitutes global explanations

{{% /col %}}

{{% col %}}

### **Limitations**

- many methods for tabular data as input, very few for images

- high dimensional datasets could lead to poorly readable rules

- high variable input spaces could do the same

{{% /col %}}

{{% /multicol %}}

{{% /section %}}

---

{{< slide id="ski" >}}

# Symbolic Knowledge Injection (SKI)

How to inject symbolic knowledge into sub-symbolic predictors

---

{{% section %}}

## Definition and Motivation (pt. 1)


> Any algorithmic procedure affecting how sub-symbolic predictors draw their inferences in such a way that predictions are either _computed_ as a function of, or _made consistent_ with, some given symbolic knowledge.

---

## Definition and Motivation (pt. 2)

- **Improve predictive performance**: by injecting symbolic knowledge, we can
  - _guide_ the learning process in order to _penalise_ inconsistencies with the symbolic knowledge, or
  - _structure_ the model's architecture to _mimic_ the symbolic knowledge

- **Enhance interpretability**: with SKI we can make predictors that are
  - interpretable by _transparent box design_, as they are built to mimic symbolic knowledge
  - interpretable using _symbols as constraints_, as they are built to respect symbolic knowledge

- **Robustness to data degradation**: symbolic knowledge can help sub-symbolic models maintain performance even in the presence of noisy or scarcity of data

- **Enhance fairness**: by incorporating symbolic knowledge about fairness constraints, we can ensure that sub-symbolic models make decisions that align with ethical considerations

- **And more**: SKI can simplify the predictor's architecture, in particular it can reduce the number of weights in a neural network, thus improving its efficiency and reducing the risk of overfitting

---

## Concepts
Main entities and how to inject symbolic knowledge into sub-symbolic predictors

---

## Entities

- **Predictor**: a sub-symbolic model that makes predictions based on input data, usually a neural network

- **Symbolic knowledge**: structured, formal knowledge that can be represented in a symbolic form. The most common forms of symbolic knowledge are
  - _Propositional logic_, simple rules with if-then structure
  - _Datalog_, a subset of first-order logic with no function symbols, only constants and variables

- **Fuzzification**: the process of converting symbolic knowledge into a form that can be used by sub-symbolic predictors, e.g. by assigning degrees of truth to symbolic statements

- **Injector**: the main component that injects symbolic knowledge into the predictor, by modifying its architecture, its training process or by other means

---

## Structuring


{{< image src="./images/workflow-structuring.svg" alt="Overview of structuring injection mechanism" width="80%" >}}

---

## Constraining

{{< image src="./images/workflow-constraining.svg" alt="Overview of constraining injection mechanism" width="80%" >}}

---

## Embedding

{{< image src="./images/workflow-embedding.svg" alt="Overview of embedding injection mechanism" width="80%" >}}

{{% /section %}}

---

{{% section %}}

## Knowledge Injection via Network Structuring (KINS)
(ref. [Magnini et al., 2023](https://doi.org/10.1093/LOGCOM/EXAD037))

---

## Fuzzification

| Formula                  | C. interpretation                                      | Formula                                       | C. interpretation                      |
|--------------------------|--------------------------------------------------------|-----------------------------------------------|----------------------------------------|
| $[[ \neg \phi ]]$        | $\eta(1 - [[ \phi ]])$                                 | $[[ \phi \le \psi ]]$                         | $\eta(1 + [[ \psi ]] - [[ \phi ]])$    |
| $[[ \phi \wedge \psi ]]$ | $\eta(\min([[ \phi ]], [[ \psi ]]))$                   | $[[ class(\bar{X}, {y}_i) \leftarrow \psi ]]$ | $[[ \psi ]]^{*}$                       |
| $[[ \phi \vee \psi ]]$   | $\eta(\max([[ \phi ]], [[ \psi ]]))$                   | $[[ \text{expr}(\bar{X}) ]]$                  | $\text{expr}([[ \bar{X} ]])$           |
| $[[ \phi = \psi ]]$      | $\eta([[ \neg( \phi \ne \psi ) ]])$                    | $[[ \mathtt{true} ]]$                         | $1$                                    |
| $[[ \phi \ne \psi ]]$    | $\eta(\| [[ \phi ]] - [[ \psi ]]\|)$                   | $[[ \mathtt{false} ]]$                        | $0$                                    |
| $[[ \phi > \psi ]]$      | $\eta(\max(0, \frac{1}{2} + [[ \phi ]] - [[ \psi ]]))$ | $[[ X ]]$                                     | $x$                                    |
| $[[ \phi \ge \psi ]]$    | $\eta(1 + [[ \phi ]] - [[ \psi ]])$                    | $[[ k ]]$                                     | $k$                                    |
| $[[ \phi < \psi ]]$      | $\eta(\max(0, \frac{1}{2} + [[ \psi ]] - [[ \phi ]]))$ | $[[ p(\bar{X}) ]]^{**}$                       | $[[ \psi_1 \vee \ldots \vee \psi_k ]]$ |


> $^{*}$ encodes the value for the $i^{\text{th}}$ output
> $^{**}$ assuming $p$ is defined by $k$ clauses of the form:
> ${p}(\bar{X}) \leftarrow \psi_1,\ \ldots,\ {p}(\bar{X}) \leftarrow \psi_k$

---

## Injector (pt.1)

{{< image src="./images/neurons.svg" alt="Example of one possible mapping between the continuous interpretation of a symbolic formula and the neurons" width="80%" >}}

---

## Injector (pt. 2)

{{< image src="./images/net-architecture.svg" alt="Example of a neural network architecture with an injector" width="80%" >}}

{{% /section %}}

---

{{% section %}}

## Knowledge Injection via Lambda Layer (KILL)
(ref. [Magnini et al., 2022](https://ceur-ws.org/Vol-3261/paper5.pdf))

---

## Fuzzification

| **Formula**              | **C. interpretation**                                |   | **Formula**                                         | **C. interpretation**                |
|--------------------------|------------------------------------------------------|---|-----------------------------------------------------|--------------------------------------|
| $[[\neg \phi]]$          | $\eta(1 - [[\phi]])$                                 |   | $[[\phi \le \psi]]$                                 | $\eta([[\phi]] - [[\psi]])$          |
| $[[\phi \wedge \psi]]$   | $\eta(\max([[\phi]], [[\psi]]))$                     |   | $[\mathrm{class}(\bar{X}, {y}_i) \leftarrow \psi]]$ | $[[\psi]]^{*}$                       |
| $[[\phi \vee \psi]]$     | $\eta(\min([[\phi]], [[\psi]]))$                     |   | $[\text{expr}(\bar{X})]]$                           | $\text{expr}([[\bar{X}]])$           |
| $[[\phi = \psi]]$        | $\eta(\left\lvert [[\phi]] - [[\psi]] \right\rvert)$ |   | $[[\mathtt{true}]]$                                 | $0$                                  |
| $[[\phi \ne \psi]]$      | $[[\neg(\phi = \psi)]]$                              |   | $[[\mathtt{false}]]$                                | $1$                                  |
| $[[\phi > \psi]]$        | $\eta(\frac{1}{2} - [[\phi]] + [[\psi]])$            |   | $[[X]]$                                             | $x$                                  |
| $[[\phi \ge \psi]]$      | $\eta([[\psi]] - [[\phi]])$                          |   | $[[{k}]]$                                           | $k$                                  |
| $[[\phi < \psi]]$        | $\eta(\frac{1}{2} + [[\phi]] - [[\psi]])$            |   | $[\mathrm{p}(\bar{X})]]^{**}$                       | $[[\psi_1 \vee \ldots \vee \psi_k]]$ |

> $^{*}$ encodes the penalty for the $i^{\text{th}}$ neuron
> $^{**}$ assuming predicate $p$ is defined by $k$ clauses of the form:
> ${p}(\bar{X}) \leftarrow \psi_1,\ \ldots,\ {p}(\bar{X}) \leftarrow \psi_k$

---

## Injector (pt.1)

*Cost function*: whenever the neural network wrongly predicts a class and violates the prior knowledge a cost proportional to the violation is added.
In this way the output of the network differs more from the expected one and this affects the back propagation step.
<br><br>
<div style="border: 1px solid #ddd; padding: 1em; background-color: #f9f9f9; border-radius: 8px; overflow-x: auto;">
$$
\begin{aligned}
Y' &= f(Y, \mathrm{cost}) \\\\
f &= Y \times (\mathbf{1} + \mathrm{cost}) \\\\
\mathrm{cost}(X, Y) &= \eta(\mathrm{p}(X) - (\mathbf{1} - Y)) \quad \text{(}\mathbf{1} - Y\text{ because 0 means true)}
\end{aligned}
$$
</div>

---

## Injector (pt. 2)

{{< image src="./images/lambda-layer.svg" alt="Example of a neural network architecture with a lambda layer" width="80%" >}}

{{% /section %}}

---

{{% section %}}

## PHDS classification task


{{% multicol %}}

{{% col %}}

<div style="margin-top: 25vh; margin-left: 5vw;">

The poker hand data set (PHDS) (cf. [Cattral Robert and Oppacher Franz, 2002](https://doi.org/10.24432/C5KW38))

- Each record represents one poker hand

- 5 cards identified by 2 values: suit and rank

- Classes: 10

- Training set: 25,010

- Test set: 1,000,000

</div>

{{% /col %}}

{{% col %}}

| **id** | **S1** | **R1** | **S2** | **R2** | **S3** | **R3** | **S4** | **R4** | **S5** | **R5** | **class** |
|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|-----------|
| 1      | 1      | 10     | 1      | 11     | 1      | 13     | 1      | 12     | 1      | 1      | 9         |
| 2      | 2      | 11     | 2      | 13     | 2      | 10     | 2      | 12     | 2      | 1      | 9         |
| 3      | 3      | 12     | 3      | 11     | 3      | 13     | 3      | 10     | 3      | 1      | 9         |
| 4      | 4      | 10     | 4      | 11     | 4      | 1      | 4      | 13     | 4      | 12     | 9         |
| 5      | 4      | 1      | 4      | 13     | 4      | 12     | 4      | 11     | 4      | 10     | 9         |
| 6      | 1      | 2      | 1      | 4      | 1      | 5      | 1      | 3      | 1      | 6      | 8         |
| 7      | 1      | 9      | 1      | 12     | 1      | 10     | 1      | 11     | 1      | 13     | 8         |
| 8      | 2      | 1      | 2      | 2      | 2      | 3      | 2      | 4      | 2      | 5      | 8         |
| 9      | 3      | 5      | 3      | 6      | 3      | 9      | 3      | 7      | 3      | 8      | 8         |
| 10     | 4      | 1      | 4      | 4      | 4      | 2      | 4      | 3      | 4      | 5      | 8         |
| 11     | 1      | 1      | 2      | 1      | 3      | 9      | 1      | 5      | 2      | 3      | 1         |
| 12     | 2      | 6      | 2      | 1      | 4      | 13     | 2      | 4      | 4      | 9      | 0         |
| 13     | 1      | 10     | 4      | 6      | 1      | 2      | 1      | 1      | 3      | 8      | 0         |
| 14     | 2      | 13     | 2      | 1      | 4      | 4      | 1      | 5      | 2      | 11     | 0         |
| 15     | 3      | 8      | 4      | 12     | 3      | 9      | 4      | 2      | 3      | 2      | 1         |


{{% /col %}}

{{% /multicol %}}

---

## An unbalanced dataset

{{% multicol %}}

{{% col %}}

{{< image src="./images/injection_files/injection_10_0.png" alt="Class distribution of the PHDS dataset (training)" width="90%" >}}

{{% /col %}}

{{% col %}}

{{< image src="./images/injection_files/injection_11_0.png" alt="Class distribution of the PHDS dataset (test)" width="90%" >}}

{{% /col %}}

{{% /multicol %}}

---

## Logic rules to inject (pt. 1)

| **Class**     | **Logic Formulation**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Pair**      | `class(R₁, ..., S₅, pair) ← pair(R₁, ..., S₅)`<br>`pair(R₁, ..., S₅) ← R₁ = R₂`<br>`pair(R₁, ..., S₅) ← R₁ = R₃`<br>`pair(R₁, ..., S₅) ← R₁ = R₄`<br>`pair(R₁, ..., S₅) ← R₁ = R₅`<br>`pair(R₁, ..., S₅) ← R₂ = R₃`<br>`pair(R₁, ..., S₅) ← R₂ = R₄`<br>`pair(R₁, ..., S₅) ← R₂ = R₅`<br>`pair(R₁, ..., S₅) ← R₃ = R₄`<br>`pair(R₁, ..., S₅) ← R₃ = R₅`<br>`pair(R₁, ..., S₅) ← R₄ = R₅`                                                                                                                                                                                                                                                                                                           |


---

## Logic rules to inject (pt. 2)

| **Class**     | **Logic Formulation**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Two Pairs** | `class(R₁, ..., S₅, two) ← two(R₁, ..., S₅)`<br>`two(R₁, ..., S₅) ← R₁ = R₂ ∧ R₃ = R₄`<br>`two(R₁, ..., S₅) ← R₁ = R₃ ∧ R₂ = R₄`<br>`two(R₁, ..., S₅) ← R₁ = R₄ ∧ R₂ = R₃`<br>`two(R₁, ..., S₅) ← R₁ = R₂ ∧ R₃ = R₅`<br>`two(R₁, ..., S₅) ← R₁ = R₃ ∧ R₃ = R₅`<br>`two(R₁, ..., S₅) ← R₁ = R₅ ∧ R₂ = R₃`<br>`two(R₁, ..., S₅) ← R₁ = R₂ ∧ R₄ = R₅`<br>`two(R₁, ..., S₅) ← R₁ = R₄ ∧ R₂ = R₅`<br>`two(R₁, ..., S₅) ← R₁ = R₅ ∧ R₂ = R₄`<br>`two(R₁, ..., S₅) ← R₁ = R₃ ∧ R₄ = R₅`<br>`two(R₁, ..., S₅) ← R₁ = R₄ ∧ R₃ = R₅`<br>`two(R₁, ..., S₅) ← R₁ = R₅ ∧ R₃ = R₄`<br>`two(R₁, ..., S₅) ← R₂ = R₃ ∧ R₄ = R₅`<br>`two(R₁, ..., S₅) ← R₂ = R₄ ∧ R₃ = R₅`<br>`two(R₁, ..., S₅) ← R₂ = R₅ ∧ R₃ = R₄` |

---

## Logic rules to inject (pt. 3)

| **Class**           | **Logic Formulation**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Three of a Kind** | `class(R₁, ..., S₅, three) ← three(R₁, ..., S₅)`<br>`three(R₁, ..., S₅) ← R₁ = R₂ ∧ R₁ = R₃`<br>`three(R₁, ..., S₅) ← R₁ = R₂ ∧ R₁ = R₄`<br>`three(R₁, ..., S₅) ← R₁ = R₂ ∧ R₁ = R₅`<br>`three(R₁, ..., S₅) ← R₁ = R₃ ∧ R₁ = R₄`<br>`three(R₁, ..., S₅) ← R₁ = R₃ ∧ R₁ = R₅`<br>`three(R₁, ..., S₅) ← R₁ = R₄ ∧ R₁ = R₅`<br>`three(R₁, ..., S₅) ← R₂ = R₃ ∧ R₂ = R₄`<br>`three(R₁, ..., S₅) ← R₂ = R₃ ∧ R₂ = R₅`<br>`three(R₁, ..., S₅) ← R₂ = R₄ ∧ R₂ = R₅`<br>`three(R₁, ..., S₅) ← R₃ = R₄ ∧ R₃ = R₅` |
| **Flush**           | `class(R₁, ..., S₅, flush) ← flush(R₁, ..., S₅)`<br>`flush(R₁, ..., S₅) ← S₁ = S₂ ∧ S₁ = S₃ ∧ S₁ = S₄ ∧ S₁ = S₅`                                                                                                                                                                                                                                                                                                                                                                                         |


---

## Training the models (pt. 1)

{{% multicol %}}

{{% col %}}

```python
class PokerNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(FEATURE_NUMBER, HIDDEN_SIZE),
            nn.ReLU(),
            nn.Linear(HIDDEN_SIZE, HIDDEN_SIZE),
            nn.ReLU(),
            nn.Linear(HIDDEN_SIZE, CLASS_NUMBER)
        )

    def forward(self, x):
        return self.model(x)
```

{{% /col %}}

{{% col %}}

```python
def rule_high_card(x_batch_orig, pred_logits):
    ranks = x_batch_orig[:, 1::2].int()  # Extract ranks from the input
    num_pairs = count_occurrences(ranks, 2)  # Count occurrences of pairs
    is_high_card = (num_pairs == 0)  # Check if there are no pairs
    prob_high_card = torch.softmax(pred_logits, dim=1)[:, 0]  # Probability of "High Card"
    penalty = ((1 - prob_high_card) ** 2) * is_high_card.float()  # Calculate penalty
    return penalty.mean()

def rule_one_pair(x_batch_orig, pred_logits):
    ranks = x_batch_orig[:, 1::2].int()  # Extract ranks from the input
    num_pairs = count_occurrences(ranks, 2)  # Count occurrences of pairs
    is_one_pair = (num_pairs == 1)  # Check if there is exactly one pair
    prob_one_pair = torch.softmax(pred_logits, dim=1)[:, 1]  # Probability of "One Pair"
    penalty = ((1 - prob_one_pair) ** 2) * is_one_pair.float()  # Calculate penalty
    return penalty.mean()
```

{{% /col %}}

{{% /multicol %}}

---

## Training the models (pt. 2)

{{< image src="./images/injection_files/injection_23_0.png" alt="Loss during training" width="100%" max-h="60vh" >}}

---

## Results

{{< image src="./images/injection_files/injection_26_0.png" alt="F1 score per class" width="100%" max-h="60vh" >}}

---

Jupyter notebook available here

[github.com/MatteoMagnini/demo-2025-woa-nesy/blob/master/notebook/injection.ipynb](https://github.com/MatteoMagnini/demo-2025-woa-nesy/blob/master/notebook/injection.ipynb)

{{< image src="./images/ski-notebook-qr.svg" alt="QR code to the Jupyter notebook" width="20%" >}}



{{% /section %}}

---

{{% section %}}

## Taxonomy of SKI methods (pt. 1)

{{< image src="./images/ski-taxonomy.svg" alt="Taxonomy of SKI methods" width="80%" >}}

---

## Taxonomy of SKI methods (pt. 2)

- **input knowledge**: how is the knowledge to-be-injected represented?
  - commonly, some sub-set of first-order logic (FOL)

- **target predictor**: which predictors can knowledge be injected into?
  - mostly, neural networks

- **strategy**: how does injection actually work?
  - _guided learning_: the input knowledge is used to _guide the training_ process
  - _structuring_: the _internal_ composition of the predictor is _(re-)structured_ to reflect the input knowledge
  - _embedding_: the input knowledge is _converted_ into numeric array form

- **purpose**: why is knowledge injected in the first place?
  - _knowledge manipulation_: improve / extend / reason about symbol knowledge—subsymbolically
  - _learning support_: improve the sub-symbolic predictor (e.g. speed, size, etc.)

---

## Discussion

{{% multicol %}}

{{% col %}}

<h3 style="text-align: center; color: blue">
Notable remarks
</h3>

- Knowledge should express relations about input-output pairs

- embedding implies _extensional_ representation of knowledge

- guided learning and structuring support _intensional_ knowledge

- propositional knowledge implies binarising the I/O space

{{% /col %}}

{{% col %}}

<h3 style="text-align: center; color: blue">
Limitations
</h3>

- Recursive data structures are natively not supported

- extensional representation cost storage

- guided learning works poorly with lacking data

{{% /col %}}

{{% /multicol %}}

{{% /section %}}

---

{{< slide id="applications" >}}

# NeSy applications with LLMs

Last recent works on Neural-Symbolic AI involve Large Language Models

---

{{% section %}}

## LLMs as oracles for instantiating ontologies with domain-specific knowledge

(ref. [Ciatto et al., 2025](https://doi.org/10.1016/J.KNOSYS.2024.112940))

{{< image src="./images/llm/llm4kg-roadmap.svg" alt="Overview of LLM4KG" width="70%" >}}

---

## Experiments

{{< image src="./images/llm/ontology_skeleton.svg" alt="Ontology skeleton" width="80%" >}}

---

## Results

{{< image src="./images/llm/llm4kg-results.png" alt="Results of LLM4KG" width="80%" >}}

{{% /section %}}


---

{{% section %}}  

## Actively Learning EL Terminologies from LLMs (pt. 1)

(ref. [Magnini et al., 2025](https://doi.org/10.3233/FAIA251009))

{{< image src="./images/llm/queries-example.svg" alt="Example of the types of queries" width="80%" >}}

---

## Actively Learning EL Terminologies from LLMs (pt. 2)

{{< image src="./images/llm/algorithm.svg" alt="Overview of the active learning algorithm" width="60%" >}}

---

## Experiments and Results (pt. 1)

{{% multicol %}}

{{% col %}}

| **Ontology**    | **$N_C$** | **$N_R$** | **Log. Ax.** | **PAC Sample** | **Poss. Ax.** |
|-----------------|-----------|-----------|--------------|----------------|---------------|
| **Animals**     | 17        | 4         | 12           | 542            | 6,936         |
| **Cell**        | 22        | 0         | 24           | 1,119          | 10,164        |
| **Football**    | 10        | 3         | 9            | 341            | 1,500         |
| **Generations** | 20        | 4         | 18           | 847            | 10,800        |
| **University**  | 7         | 3         | 4            | 139            | 588           |

<br>
Ontology statistics and PAC sample sizes with $\epsilon=0.2$ and $\gamma=0.1$. $N_C$ and $N_R$ are the number of concept and role names occurring in the ontologies.

{{% /col %}}

{{% col %}}

| **Ontology**     | **Accuracy** | **Recall** | **Precision** | **F1-Score** |
|-------------------|--------------|------------|---------------|--------------|
| **Animals**       | 0.737        | 0.858      | 0.381         | 0.428        |
| **Cell**          | 0.391        | 0.733      | 0.206         | 0.284        |
| **Football**      | 0.553        | 0.890      | 0.422         | 0.477        |
| **Generations**   | 0.691        | 0.658      | 0.564         | 0.476        |
| **University**    | 0.622        | 0.629      | 0.313         | 0.302        |

<br>
Results of ExactLearner+LLM grouped by ontologies.

{{% /col %}}

{{% /multicol %}}

---

## Experiments and Results (pt. 2)

{{% multicol %}}

{{% col %}}

| **Model**         | **Accuracy** | **Recall** | **Precision** | **F1-Score** |
|-------------------|--------------|------------|---------------|--------------|
| **Llama2 (13b)**  | 0.521        | 0.71       | 0.294         | 0.314        |
| **Llama3 (8b)**   | 0.43         | 0.947      | 0.218         | 0.333        |
| **Mistral (7b)**  | 0.741        | 0.747      | 0.45          | 0.49         |
| **Mixtral (47b)** | 0.705        | 0.611      | 0.547         | 0.436        |

<br>
Results of ExactLearner+LLM grouped by models.

{{% /col %}}

{{% col %}}

| **Prompt Type**         | **Accuracy** | **Recall** | **Precision** | **F1-Score** |
|-------------------------|--------------|------------|---------------|--------------|
| **M. OWL Syntax**       | 0.34         | 0.93       | 0.165         | 0.262        |
| **Natural Language**    | 0.751        | 0.811      | 0.414         | 0.511        |
| **A. M. OWL Syntax**    | 0.537        | 0.767      | 0.326         | 0.347        |
| **A. Natural Language** | 0.767        | 0.506      | 0.603         | 0.454        |

<br>
Results of ExactLearner+LLM grouped by prompts.

{{% /col %}}

{{% /multicol %}}

{{% /section %}}

---

## I hope you enjoyed the talk!

{{% multicol %}}


{{% col %}}

{{< image src="./images/matteo.png" alt="Matteo Magnini" width="100%" max-h="50vh" >}}

{{% /col %}}

{{% col %}}

Let's keep in touch!

<br>

📫🎓 [matteo.magnini@unibo.it](mailto:matteo.magnini@unibo.it)

<br>

📫✉️‍ [matteo.magnini00@gmail.com](mailto:matteo.magnini00@gmail.com)

<br>

💻 [github.com/MatteoMagnini](https://github.com/MatteoMagnini)

<br>

✒️ [www.linkedin.com/in/matteo-magnini/](https://www.linkedin.com/in/matteo-magnini/)


{{% /col %}}

{{% /multicol %}}