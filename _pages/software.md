---
permalink: /software/
title: "Software"
author_profile: true
redirect_from: 
  - /software/
  - /software.html
seg_vamos:
  - image_path: /software/efficient-motif.png
    title: "vamos"
    excerpt: |
      STR and VNTR annotation by motif composition for PacBio and Oxford Nanopore reads, and assemblies. The vamos suite contains two components, one to characterize the repeat motifs in a population using an `efficient` motif set, a subset of motifs that preserves motif sequence diversity while removing rare motifs, and annotation software that uses wraparound dynamic programming to annotate samples using tandem repeat and motif databases.
      https://github.com/chaissonlab/vamos

seg_lra:
  - image_path: /software/lra.png
    title: "LRA"
    excerpt: |
      Software for mapping long reads (PacBio/Oxford Nanopore) or their assemblies to genomes. LRA implements an exact convex gap penalty for biologically meaningful gaps to discover structural variation.
      https://github.com/chaissonlab/lra

---

{% include feature_row id="seg_lra" type="left" %}
