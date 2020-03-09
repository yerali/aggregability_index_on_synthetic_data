# aggregability_index_on_synthetic_data
Article: Measuring the effect of node aggregation on community detection. Yérali Gandica. Adeline Decuyper, Christophe Cloquet, Isabelle Thomas, and Jean-Charles Delvenne https://arxiv.org/pdf/1809.08855.pdf

This repository has been created to study the effect of node aggregation on community detection based on simulations. We introduce the aggregability index, a quantitative proxy for the robustness of the community structure of a given network, concerning given node aggregation classes. The codes in this repository are useful to study the
variation of the aggregability index, when the fit between the aggregation partitions and the communities at the disaggregated level decreases.

To create the topology, we start with a graph of 4 disconnected cliques of 160 nodes each (640 nodes in total), creating
a perfect partition into 4 communities. Each clique (160 nodes) is divided into 4 subsets of 40 nodes, arbitrarily. These 4 subsets are the aggregation classes. Thus, the aggregability index is η = 1, as each of the 16 aggregation class is embedded into a community.

We then, gradually rewire the links so that the 4 cliques start to mix. In this way, the community structure gradually ceases to be the union of aggregation classes, which are always fixed.

In the repository, running the script_stat.sh contains all the codes to create the original topology, to rewire, calculating community detection and averaging values. Each program is easily identified by its name.

Please, any question/concern/suggestion is welcome at the email ygandica@gmail.com
