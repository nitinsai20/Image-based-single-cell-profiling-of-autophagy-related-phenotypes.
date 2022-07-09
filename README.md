# Image-based-single-cell-profiling-of-autophagy-related-phenotypes.

Autophagy is an essential intracellular degradative process. Autophagy has been implicated in many diseases such as neurodegenerative diseases, cancer, and infectious diseases1. Identifying and characterizing autophagy-related phenotypes is a pivotal step in developing better therapeutics and effective regulation. Most methods currently used for characterizing autophagy are low throughput and are unable to capture the dynamic changes comprehensively. Image-based profiling serves as an unbiased quantitative approach for characterizing biological phenotypes at a high throughput scale. Image-based profiling offers many unique advantages such as single-cell resolution and the ability to monitor temporal changes with preserved spatial information. Example images are provided below showing different morphology under drug treatments. 
![image](https://user-images.githubusercontent.com/54224066/178123474-4464491a-6446-4401-a704-17dc7d398bad.png)


We developed a new computational pipeline by combining [Cellpose](https://github.com/MouseLand/cellpose) and [bTrack](https://github.com/quantumjot/BayesianTracker) algorithms. Additionally, we developed our own in-house pipeline for extracting morphological features at a single cell level. 


https://user-images.githubusercontent.com/54224066/178123626-03ada7c2-974b-41d3-bb84-1c34a2dfda43.mp4




We identify the key image features that capture the variability in cellular morphology under different autophagy modulators. Moreover, using these image features we also differentiate various kinds of autophagy perturbations. This approach can be used for characterizing phenotypes and understanding the mechanism of action. Furthermore, this work would act as a proof of principle for developing image-based high throughput drug screening technologies. In future work, similar analysis can be expanded for quantifying morphological changes in other organelles such as the mitochondria and lysosomes for characterizing disease state and progression. 
