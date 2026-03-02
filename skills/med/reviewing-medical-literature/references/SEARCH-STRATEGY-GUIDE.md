# Medical Literature Search Strategy Guide

## Database Selection

| Database | Best For | Access |
|----------|---------|--------|
| **PubMed/MEDLINE** | Biomedical literature, clinical studies | Free |
| **Cochrane Library** | Systematic reviews, meta-analyses | Subscription (abstracts free) |
| **EMBASE** | European literature, pharmacology, broader coverage | Subscription |
| **CINAHL** | Nursing and allied health | Subscription |
| **PsycINFO** | Psychology and behavioral sciences | Subscription |
| **Google Scholar** | Broad initial search, citation tracking | Free |

## MeSH (Medical Subject Headings) Strategy

### Building a Search

1. **Identify concepts** from PICO elements
2. **Find MeSH terms** for each concept (use MeSH Browser)
3. **Add free-text synonyms** to catch non-indexed articles
4. **Combine with Boolean operators**

### Example Build

**Clinical question**: Does exercise reduce falls in elderly patients?

| Concept | MeSH Terms | Free Text |
|---------|-----------|-----------|
| Population | "Aged" [MeSH] | elderly OR older adult* OR geriatric |
| Intervention | "Exercise" [MeSH] OR "Exercise Therapy" [MeSH] | physical activity OR exercise program* |
| Outcome | "Accidental Falls" [MeSH] | fall* OR falling |

**Combined**: (MeSH + free text for each concept) AND together

## Search Filters

### Study Design Filters

| To Find | PubMed Filter |
|---------|--------------|
| RCTs only | "Randomized Controlled Trial" [pt] |
| Systematic reviews | "Systematic Review" [pt] OR "Meta-Analysis" [pt] |
| Clinical trials | "Clinical Trial" [pt] |
| Guidelines | "Practice Guideline" [pt] |

### Quality Filters (PubMed Clinical Queries)

| Category | Sensitivity vs. Specificity |
|----------|---------------------------|
| Therapy | Broad (sensitive) catches more; Narrow (specific) catches best |
| Diagnosis | Same trade-off |
| Prognosis | Same trade-off |
| Etiology | Same trade-off |

## Common Search Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| Only MeSH, no free text | Misses unindexed articles | Always include synonyms |
| Only free text, no MeSH | Lower precision, misses related terms | Use MeSH for core concepts |
| Too many ANDs | Over-restricts results | Start broad, narrow incrementally |
| Not exploding MeSH | Misses narrower terms | Use [MeSH] which auto-explodes in PubMed |
| Date limits without reason | Misses landmark studies | Only limit when justified (new drug, updated guideline) |
| English only | Misses international research | Include unless resources prohibit translation |

## Documenting the Search

Always record:
- Database(s) searched
- Date of search
- Exact search string (copy from search history)
- Filters applied
- Number of results
- Screening criteria (inclusion/exclusion)
- PRISMA flow diagram for systematic reviews
