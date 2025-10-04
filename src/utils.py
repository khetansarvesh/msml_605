from typing import Tuple
from src.models.linear_interpolation import LinearInterpolationModel
from src.models.stupid_backoff import StupidBackoffModel

def find_optimal_lambdas(train_text: str, dev_text: str) -> Tuple[float, float, float]:
    """
    Find the optimal lambda values for linear interpolation using development data.
    Args:
        train_text (str): Training text.
        dev_text (str): Development/validation text.
    Returns:
        Tuple[float, float, float]: The best (lambda1, lambda2, lambda3) values.
    """
    best_perplexity = float('inf')
    best_lambdas = (0.33, 0.33, 0.34)
    lambda_combinations = [
        (0.1, 0.2, 0.7), (0.1, 0.3, 0.6), (0.1, 0.4, 0.5),
        (0.2, 0.2, 0.6), (0.2, 0.3, 0.5), (0.2, 0.4, 0.4),
        (0.3, 0.3, 0.4), (0.3, 0.4, 0.3), (0.4, 0.4, 0.2),
        (0.33, 0.33, 0.34), (0.25, 0.25, 0.5), (0.5, 0.25, 0.25)
    ]
    for lambda1, lambda2, lambda3 in lambda_combinations:
        model = LinearInterpolationModel(lambda1, lambda2, lambda3)
        model.train(train_text)
        perplexity = model.calculate_perplexity(dev_text)
        if perplexity < best_perplexity:
            best_perplexity = perplexity
            best_lambdas = (lambda1, lambda2, lambda3)
    return best_lambdas

def find_optimal_alpha(train_text: str, dev_text: str) -> float:
    """
    Find the optimal alpha value for Stupid Backoff using development data.
    Args:
        train_text (str): Training text.
        dev_text (str): Development/validation text.
    Returns:
        float: The best alpha value.
    """
    best_perplexity = float('inf')
    best_alpha = 0.4
    alpha_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    for alpha in alpha_values:
        model = StupidBackoffModel(alpha)
        model.train(train_text)
        perplexity = model.calculate_perplexity(dev_text)
        if perplexity < best_perplexity:
            best_perplexity = perplexity
            best_alpha = alpha
    return best_alpha

def load_penn_treebank_data():
    """
    Load sample Penn Treebank data for demonstration purposes.
    Returns:
        Tuple[str, str, str]: (train_text, dev_text, test_text)
    """
    train_text = """
    The quick brown fox jumps over the lazy dog. The dog was sleeping peacefully. 
    A cat walked by the sleeping dog. The fox ran away quickly. The dog woke up.
    The cat and the dog became friends. They played together in the garden.
    The sun was shining brightly. Birds were singing in the trees.
    The garden was full of beautiful flowers. The children were playing happily.
    """
    dev_text = """
    The dog barked loudly at the mailman. The mailman delivered the letters.
    The children were reading books in the library. The books were very interesting.
    The teacher explained the lesson clearly. The students listened carefully.
    """
    test_text = """
    The weather was perfect today. The birds were flying high in the sky.
    The students were studying for their exams. The library was very quiet.
    The teacher gave the students homework. The homework was quite difficult.
    """
    return train_text, dev_text, test_text
