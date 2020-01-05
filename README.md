# Fuzzy-Matching-Deduplication

This program allows for the deduplication of fuzzy matches in a pandas dataframe using the fuzzywuzzy package. Each row is matched to the whole list of values in a column, and the top three matches for each row are populated to separate columns that indicate the match value and its Levenshtein Distance (LD) score.

These matches can then be manually reviewed in order to set an appropriate LD score cutoff for deduplication. 
