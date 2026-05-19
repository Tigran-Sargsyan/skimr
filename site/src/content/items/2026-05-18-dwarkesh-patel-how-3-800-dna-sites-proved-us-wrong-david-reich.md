---
title: How 3,800 DNA Sites Proved Us Wrong – David Reich
author: Dwarkesh Patel
source_id: 2
source_slug: dwarkesh-patel
url: https://www.youtube.com/watch?v=dEYA-zKAPfc
published_at: '2026-05-18T16:43:48Z'
duration_seconds: null
primary_theme: science
secondary_theme: thinking
relevance: 8
hook: Ancient DNA reveals thousands of recent human adaptations once thought nonexistent.
tldr: David Reich describes how ancient DNA repeatedly overturned his prior beliefs about human evolution. Initial studies suggested very few recent selection events, reinforcing the idea that natural selection was mostly quiescent in modern humans. A massively expanded dataset and new statistical methods instead revealed thousands of confidently supported sites under selection, many tied to measurable traits.
caveats: Skip it if you want immediate engineering takeaways; this is mostly population genetics and method-driven scientific revision, not AI systems or applied software.
pitch: You should listen if you want a concrete example of how better data and better inference can overturn a widely held scientific belief, with real numbers, statistical method changes, and a strong epistemic lesson about selection and human evolution.
---

## Key Points

- Reich previously believed non-African humans were just a subset of African variation with no Neanderthal admixture.
- Analysis of Neanderthal genomes showed Neanderthals are more closely related to non-Africans than to Africans, implying interbreeding.
- Early ancient DNA scans in 2015 found only about 12 strongly selected positions in Europeans and Middle Easterners.
- Even a 2024 study with much better data detected only 21 strongly differentiated positions, suggesting selection might be rare.
- Reich’s group assembled about 16,000 ancient individuals (10,000 newly reported) from Europe and the Middle East spanning 18,000 years.
- They applied a new method that predicts genotypes from a relatedness matrix and tests whether adding constant-direction selection improves prediction.
- Using this approach, they identified at least 479 sites with ≥99% confidence and roughly 3,800 sites with >50% confidence of directional selection.
- Cross-referencing with UK Biobank GWAS data showed up to a fivefold enrichment of trait-associated variants among high-selection-score sites, validating the signals as real selection targets.

## Notes

## Reich’s Changing Views and the Neanderthal Shock

- Reich emphasizes that his work has repeatedly proven his initial biases wrong, to the point he calls the experience “almost traumatizing.”
- Before working on the Neanderthal genome, he and others held a clear model: non-Africans were simply a subset of African genetic variation.
- In that framework, there was “no evidence at all” for interbreeding between Neanderthals and modern humans, nor for other archaic admixture.
- Various analyses supported the idea that non-African variation could be fully explained as a sampled subset of African diversity, with no need for admixture.
- Once Neanderthal DNA became available, his analyses showed Neanderthals were more closely related to non-Africans than to Africans.
- This implied Neanderthal introgression into ancestors of non-Africans, contradicting the prior model.
- Reich initially thought this result must be a mistake and spent years trying to make it “go away,” but the signal only became stronger.
- This earlier episode sets up a pattern: strong priors, surprising data, prolonged skepticism, and eventual acceptance.

## Initial Belief: Natural Selection Was Mostly Quiescent

- Reich reports a similar trajectory regarding natural selection in recent human evolution.
- His prior view was that natural selection had been “pretty quiescent” in our species over the last several hundred thousand years.
- Under that assumption, genetic variation in present-day populations should show relatively few signals of strong, adaptive directional selection.
- Early ancient DNA selection scans seemed to confirm this view.

## The 2015 Ancient DNA Study and Its Limits

- In 2015, Reich and colleagues (including Ian Mathieson) analyzed about 200 ancient Europeans and Middle Easterners.
- They compared allele frequencies in these ancient sources of modern Europeans to present-day Europeans.
- They looked for frequency differences too extreme to be attributed to chance, given reconstructed demographic history.
- That study identified 12 positions with highly different frequencies, interpreted as strong selection targets.
- Some of these positions had been known, others were newly identified, and the team hoped that more data would reveal many more such sites.
- Over the following decade, however, increasing sample sizes did not yield a proportional growth in discoveries.
- A large 2024 study from Copenhagen, using improved data and methods, detected only 21 strongly differentiated positions.
- While “almost twice” the 2015 count, this was disappointing relative to the dramatic increase in data quality and quantity.
- The natural interpretation was that they might be approaching an asymptote: perhaps there truly were only a limited number of strong selection events.
- This reinforced the idea that adaptive directional selection in recent human history might be genuinely rare.

## Building a Much Larger Ancient DNA Dataset

- Reich’s group then undertook a new study led by Ali Akbar, designed to radically improve power to detect selection.
- First innovation: greatly expanded data volume, increasing ancient DNA sample size by about 14-fold over prior work.
- They reported about 10,000 newly generated ancient genomes, contributing to a total of roughly 16,000 ancient individuals.
- These individuals span the last ~18,000 years and are concentrated in Europe and the Middle East.
- He notes this region is not inherently more important, but it is where 70–80% of ancient DNA data currently exists for historical reasons.
- This dense temporal series in a single broad region provides a “natural laboratory” for tracking environmental change and its impact on genomes.

## New Method: Relatedness Matrix plus Constant-Direction Selection

- Second innovation: an entirely new methodology imported from medical genetics, specifically from techniques used to find disease risk factors.
- The core idea is to predict a person’s genotype at each site based on how related that person is to all others.
- They construct a genetic relatedness matrix for about 22,000 individuals (16,000 ancient plus moderns).
- For each of 10 million positions in the genome, they predict the genotype using patterns of relatedness that capture demographic history: bottlenecks, drift, and admixture.
- This baseline model accounts for genome-wide processes that affect all loci similarly.
- They then test an alternative model in which, at a given site, natural selection has been pushing allele frequencies in the same direction across geography and time.
- In this model, a constant selection coefficient is added and they ask whether this improves prediction of observed allele frequency changes beyond what relatedness alone explains.
- Reich acknowledges this is a “dumb assumption,” since real selection pressures change over time and space.
- However, it provides a very simple, tractable null vs. alternative setup: no selection versus constant-direction selection.
- Dwarkesh summarizes the model as having two components: (1) a relatedness matrix that captures drift, bottlenecks, admixture genome-wide, and (2) a site-specific selection coefficient that, if non-zero, improves fit for allele frequency trajectories.
- Reich confirms this summary is “precisely right.”

## Discovery: Hundreds to Thousands of Selected Sites

- Applying this approach to 10 million positions in 22,000 individuals, they ask whether any sites show more consistent directional change over time than expected by chance.
- They find “many many hundreds” of positions with too much change in a consistent direction to be explained by drift and demographic history alone.
- Because selected sites can be closely spaced and statistically interfere with each other, they implement a procedure to count largely independent signals.
- By picking at most one signal per region and blanking out nearby effects, they estimate:
  - About 479 positions are independently under selection with ~99% confidence.
  - Using a more permissive threshold (>50% confidence), about 3,800 positions appear to be under directional selection.
- Reich characterizes this as a “crazy number of results,” especially compared with prior scans that yielded, at most, a couple dozen signals per scan.
- As before, the magnitude of this shift led them to suspect error, and they spent “the next couple of years” trying to invalidate the findings.
- Instead of disappearing, the signals became stronger as analyses improved.

## Independent Validation with UK Biobank and GWAS Data

- Seeking independent evidence that these candidate sites are genuinely under selection, they turned to genome-wide association study (GWAS) data.
- Specifically, they leveraged the UK Biobank: about 500,000 individuals from Great Britain measured for hundreds of traits with whole-genome data.
- For each of the 10 million positions, they checked whether it is convincingly associated with at least one trait in the UK Biobank GWAS corpus.
- Roughly 15% of all tested positions (about 1.5 million) predict at least one trait when no selection filter is applied.
- They then stratified sites by their natural selection statistic, which measures how strongly a site appears to be changing over time in a non-zero direction.
- The selection statistic can be viewed approximately as a Gaussian z-score: the number of standard deviations away from zero (zero meaning no selection).
- As they increased the threshold on this statistic (e.g., requiring it to exceed 1, 2, 3, 4, then 5), the fraction of trait-associated sites rose.
- At a threshold of about 5, there was about a fivefold enrichment of GWAS hits among high-selection-score sites.
- Instead of 15% of sites affecting at least one trait, around 60–70% of sites above this selection threshold affected traits.
- This monotonic increase and plateau provided independent confirmation that high selection scores correspond to biologically meaningful, trait-affecting variants.
- Above a selection statistic of 5, further increases did not yield additional enrichment, suggesting a ceiling: nearly all sites at that level are true positives.
- Using simulations, they validated that this pattern matches expectations if high selection scores largely represent genuine selection signals.

## Interpretation: Selection Is Far from Quiescent

- Reich’s interpretation is that once the selection statistic exceeds roughly 5, “essentially all” of these signals represent real natural selection.
- This conclusion implies that, contrary to earlier belief, recent human evolution has involved thousands of selected sites, at least in Europe and the Middle East over the last ~18,000 years.
- The shift from ~12–21 known signals to hundreds or thousands arises from both vastly increased ancient DNA sample sizes and a more powerful statistical framework.
- The work overturns the prior view of a largely quiescent recent selective landscape and suggests a rich, ongoing adaptive process affecting many traits in human populations.

