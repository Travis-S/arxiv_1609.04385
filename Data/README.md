Data Files Description
-------------------

In this directory, we provide several data files that might be of use for others.

The ``Maximum Likelihood Paper - Tomography Data.xlsx`` file contains all the data files (each file as its own sheet), as well as a variant of this ``README``. For your convenience, we have converted the sheets into ``.csv`` files, to help make it easier to use the data.

In the table below, we provide descriptions of each file.

|File Name| File Description |  Related Figures| Variable Name | Variable Description|
---------------|----------------------|------------|-----------|-----------|----------|-------------|
|states | Matrix elements of the true states used in our simulations | 2,6,11|  stateID | Label for the state  |
||||   (j, k) |  The (j, k) matrix element|   
|iso_quantum_models | Predictions of isotropic models (Wilks Theorem and our own) |2,9,11|dimRec | The Hilbert space dimension of the model|
||||rankTrue | Rank of the true state|
||||Wilks_Theorem | Value of LLRS given by the Wilks Theorem|
||||Our_Model | Value of the LLRS given by our model |
|iso_quantum_llrs_sim_totals| Results of Numerical Simulations of the Isotropic Quantum Model |2,9|dimRec | The Hilbert space dimension of the model|
||||rankTrue | Rank of the true state|
||||llrs | Numerically-averaged value of the LLRS|
||||numTrials | Number of instances we averaged over|
|iso_quantum_llrs_sim_contribs |  Individual contributions lambda_jk in the Isotropic Quantum Model | 6,13|stateID| Label for the state|
||||numTrials | Number of instances we averaged over|
||||(j, k) |  The value lambda_jk|
|heterodyne_llrs_sim_results | Numerical results for simulated heterodyne tomography   |11,12|stateID | Label for the state|
||||dimRec | The Hilbert space dimension of the model|
||||Sample | The number of heterodyne counts used in the simulation| 
||||LogLik | The average loglikelihood of the maximum loglikelihood estimate|
||||LogLik_true | The average loglikelihood of the true state|
||||rankTrue| Rank of the true state
||||numTrials | Number of heterodyne datasets the average was computed over|
|heterodyne_llrs_sim_contribs |   Individual contributions lambda_jk for heterodyne tomography |   13|stateID| Label for the state|
||||sampleSize | The number of heterodyne counts used in the simulation|
||||numTrials | Number of heterodyne datasets the average was computed over|
||||(j, k) | The value lambda_jk|
|heterodyne_condition_num   | Condition numbers of the estimated Fisher Information Matrix   | 10|stateID | Label for the state|
||||dimRec | The Hilbert space dimension of the model|
||||conditionNum | The condition number (ratio of largest eigenvalue to smallest)|
||||numTrials| Number of heterodyne datasets the average was computed over|
||||sampleSize | The number of heterodyne counts used in the simulation|
|avg_decrement|Average of numerical solutions to Equation 16|
||||avg_dec|The average value of z in Equation 16|
||||dim|Dimension of the Hilbert space|
||||numTrials| Number of instances we averaged over|
||||rankTrue: Rank of the true state|
            

            
            
            
