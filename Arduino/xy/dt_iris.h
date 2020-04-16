
    // !!! This file is generated using emlearn !!!

    #include <eml_trees.h>
    

EmlTreesNode dt_iris_nodes[11] = {
  { 3, 0.800000011920929, 1, 2 },
  { -1, 0, -1, -1 },
  { 3, 1.75, 3, 9 },
  { 2, 4.950000047683716, 4, 7 },
  { 3, 1.6500000357627869, 5, 6 },
  { -1, 1, -1, -1 },
  { -1, 2, -1, -1 },
  { 3, 1.550000011920929, 6, 8 },
  { 2, 5.450000047683716, 5, 6 },
  { 2, 4.8500001430511475, 10, 6 },
  { 1, 3.100000023841858, 6, 5 } 
};

int32_t dt_iris_tree_roots[1] = { 0 };

EmlTrees dt_iris = {
        11,
        dt_iris_nodes,	  
        1,
        dt_iris_tree_roots,
    };

static inline int32_t dt_iris_predict_tree_0(const float *features, int32_t features_length) {
          if (features[3] < 0.800000011920929) {
              return 0;
          } else {
              if (features[3] < 1.75) {
                  if (features[2] < 4.950000047683716) {
                      if (features[3] < 1.6500000357627869) {
                          return 1;
                      } else {
                          return 2;
                      }
                  } else {
                      if (features[3] < 1.550000011920929) {
                          return 2;
                      } else {
                          if (features[2] < 5.450000047683716) {
                              return 1;
                          } else {
                              return 2;
                          }
                      }
                  }
              } else {
                  if (features[2] < 4.8500001430511475) {
                      if (features[1] < 3.100000023841858) {
                          return 2;
                      } else {
                          return 1;
                      }
                  } else {
                      return 2;
                  }
              }
          }
        }
        

int32_t dt_iris_predict(const float *features, int32_t features_length) {

        int32_t votes[3] = {0,};
        int32_t _class = -1;

        _class = dt_iris_predict_tree_0(features, features_length); votes[_class] += 1;
    
        int32_t most_voted_class = -1;
        int32_t most_voted_votes = 0;
        for (int32_t i=0; i<3; i++) {

            if (votes[i] > most_voted_votes) {
                most_voted_class = i;
                most_voted_votes = votes[i];
            }
        }
        return most_voted_class;
    }
    