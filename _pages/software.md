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
      bioconda: vamos  
      git: https://github.com/chaissonlab/vamos
      publication:  
      authors: Jingwen Ren and [Bida Gu]({% link Bida_Gu.md %})  
seg_ctyper:
  - image_path: /software/ctyperlogo.png
    title: "ctyper"
    excerpt: |
      Ctyper is a genotyping approach for pangenomes to detect alleles that are shared between a biobank (short-read sequencing) sample and a long-read pangenome for challenging and copy-number variable regions of the genome.
      bioconda: ctyper  
      https://github.com/chaissonlab/ctyper

seg_lra:
  - image_path: /software/lra.png
    title: "LRA"
    excerpt: |
      Software for mapping long reads (PacBio/Oxford Nanopore) or their assemblies to genomes. LRA implements an exact convex gap penalty for biologically meaningful gaps to discover structural variation.  
      git https://github.com/chaissonlab/lra

---
{% include feature_row id="seg_ctyper" type="left" %}
{% include feature_row id="seg_vamos" type="left" %}
{% include feature_row id="seg_lra" type="left" %}
