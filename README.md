# Image-based-single-cell-profiling-of-autophagy-related-phenotypes.

Autophagy is an essential intracellular degradative process. Autophagy has been implicated in many diseases such as neurodegenerative diseases, cancer, and infectious diseases1. Identifying and characterizing autophagy-related phenotypes is a pivotal step in developing better therapeutics and effective regulation. Most methods currently used for characterizing autophagy are low throughput and are unable to capture the dynamic changes comprehensively. Image-based profiling serves as an unbiased quantitative approach for characterizing biological phenotypes at a high throughput scale. Image-based profiling offers many unique advantages such as single-cell resolution and the ability to monitor temporal changes with preserved spatial information. Example images are provided below indicating different morphology based on the king of perturbation. 

![image](https://user-images.githubusercontent.com/54224066/178125164-1d4b90d6-9203-48ca-8e79-5680006a5e6a.png)



We developed a new computational pipeline by integrating [Cellpose](https://github.com/MouseLand/cellpose) and [bTrack](https://github.com/quantumjot/BayesianTracker) algorithms. Additionally, we developed our own in-house pipeline for extracting morphological features for autophagy vesicles (puncta) and the cells. 
***Please note that we are still in the process of documenting and not all information is provided or up to date. ***


![napari_2022-07-10_00-21-20_AdobeExpress_AdobeExpress (1)](https://user-images.githubusercontent.com/54224066/178131387-e24a7a39-cf9e-40ba-a2b3-c9d15f0f0e4d.gif)


We identifed the key image features that capture the variability in cellular morphology under different autophagy modulators. Moreover, using these image features we also differentiate various kinds of autophagy perturbations. This approach can be used for characterizing phenotypes and understanding the mechanism of action. Furthermore, this work would act as a proof of principle for developing image-based high throughput drug screening technologies. In future work, similar analysis can be expanded for quantifying morphological changes in other organelles such as the mitochondria and lysosomes for characterizing disease state and progression. 

![image](https://user-images.githubusercontent.com/54224066/178125135-abd0ccc7-8364-40c2-a9d4-ba4aaedc959b.png)
