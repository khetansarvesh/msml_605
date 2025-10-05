### 1. Training MLE Models
MLE 1-gram perplexity: 691.4702433653597  
MLE 2-gram perplexity: inf  
MLE 3-gram perplexity: inf  
MLE 4-gram perplexity: inf

### 2. Training Add-1 Smoothed Trigram Model
Add-1 smoothed trigram perplexity: 2930.2797642476817

### 3. Training Linear Interpolation Model
Optimal lambdas: (0.4, 0.4, 0.2)
Linear interpolation perplexity: 213.37374001604283

### 4. Training Stupid Backoff Model
Optimal alpha: 0.9  
Stupid backoff perplexity: 92.10757584975707

### 5. Generating Text

Generated Sentences:
1. yen yesterday 's composite trading under <unk> sierra chemical economic president my car maker jaguar but figures for september fired
2. <unk> neither side savings its board <unk> big brains our big chicken stores in the it cents federal the issue
3. green won a kept engine plant but at least and exchange commission mr that he and <unk> now as campaign
4. <unk> said fk-506 will said separately of <unk> field calif sterling n from being a <unk> company mobil is preparing
5. <unk> teaches government agencies in frankfurt zurich and production restraint by dow jones november n rehabilitation share the big of

### 6.1. Pre-processing and Vocabulary Decisions
* Tokenization was performed by splitting text on whitespace and punctuation, converting all text to lowercase. Sentence boundaries were marked using special tokens (e.g., `<s>`, `</s>`). Unknown words were replaced with `<unk>` to handle out-of-vocabulary terms. This ensures consistent input for all models and reduces vocabulary size.

### 6.2. Impact of N-gram Order
* The perplexity results show that as the order of the n-gram increases, the perplexity for unsmoothed models becomes infinite due to data sparsity: many higher-order n-grams are unseen in the test set. This is a direct consequence of the Markov Assumption, which limits context, and the limited size of the training data, which cannot cover all possible n-grams.

### 6.3. Comparison of Smoothing/Backoff Strategies
* Smoothing and backoff strategies significantly reduce perplexity compared to unsmoothed models. Add-1 smoothing lowers perplexity but can still over-penalize rare events. Linear interpolation and stupid backoff perform better, with stupid backoff achieving the lowest perplexity. This is because these methods better balance the use of higher- and lower-order n-grams, mitigating data sparsity.
* The unsmoothed models have high or infinite perplexity because they assign zero probability to unseen n-grams. Smoothing assigns a small probability to all possible n-grams, preventing zero probabilities. Backoff/interpolation strategies combine information from multiple n-gram orders, further improving performance. Stupid backoff performed best due to its effective use of lower-order statistics when higher-order counts are sparse.

### 6.4. Qualitative Analysis (Generated Text)
The generated text is somewhat fluent and captures some local word dependencies, but lacks global coherence and can produce ungrammatical or nonsensical phrases. This is typical for n-gram models, which only consider limited context. The use of backoff allows the model to generate plausible word sequences even when higher-order n-grams are missing.