# emojivote

Propose reading group papers on `slack`. Formatted _with style_.


## Installation

```bash
git clone https://github.com/andreasgrv/emojivote
cd emojivote
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
pip install .
```

## Get formatted output

1. Run the installed command, passing a list of links to the papers you want on arxiv.

```bash
emojivote-slack --paper-links https://arxiv.org/abs/2102.11582 https://arxiv.org/abs/math/9701207
```

This should output (emoji selection is random):

>
    :ocean: *Deterministic Neural Networks with Inductive Biases Capture Epistemic and Aleatoric Uncertainty*
    _Mukhoti, Jishnu, Kirsch, Andreas, van Amersfoort, Joost, Torr, Philip H. S., Gal, Yarin_
    https://arxiv.org/pdf/2102.11582.pdf
    We show that a single softmax neural net with minimal changes can beat the
    uncertainty predictions of Deep Ensembles and other more complex
    single-forward-pass uncertainty approaches. Standard softmax neural nets suffer
    from feature collapse and extrapolate arbitrarily for OoD points. This results
    in arbitrary softmax entropies for OoD points which can have high entropy, low,
    or anything in between, thus cannot capture epistemic uncertainty reliably. We
    prove that this failure lies at the core of "why" Deep Ensemble Uncertainty
    works well. Instead of using softmax entropy, we show that with appropriate
    inductive biases softmax neural nets trained with maximum likelihood reliably
    capture epistemic uncertainty through their feature-space density. This density
    is obtained using simple Gaussian Discriminant Analysis, but it cannot
    represent aleatoric uncertainty reliably. We show that it is necessary to
    combine feature-space density with softmax entropy to disentangle uncertainties
    well. We evaluate the epistemic uncertainty quality on active learning and OoD
    detection, achieving SOTA ~98 AUROC on CIFAR-10 vs SVHN without fine-tuning on
    OoD data.

    :snowflake: *Piles of Cubes, Monotone Path Polytopes and Hyperplane Arrangements*
    _Athanasiadis, Christos A._
    https://arxiv.org/pdf/math/9701207.pdf
    Monotone path polytopes arise as a special case of the construction of fiber
    polytopes, introduced by Billera and Sturmfels. A simple example is provided by
    the permutahedron, which is a monotone path polytope of the standard unit cube.
    The permutahedron is the zonotope polar to the braid arrangement. We show how
    the zonotopes polar to the cones of certain deformations of the braid
    arrangement can be realized as monotone path polytopes. The construction is an
    extension of that of the permutahedron and yields interesting connections
    between enumerative combinatorics of hyperplane arrangements and geometry of
    monotone path polytopes.


2. Paste the above into Slack and use `Ctrl+Shift+F` to Format them message.
