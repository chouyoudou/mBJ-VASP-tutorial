## mBJ-tutorial
Tutorial of mBJ calculation in VASP

You need to install vaspkit first
https://vaspkit.com/

* (I) structure relaxation

* (II) PBE band calculation based on the relaxed structure
  * (a) self-consistent (SCF) calculation [10_scf_cal].
  * (b) band calculation based on converged charge density at (II-a) [11_band_cal].
    * Use vaspkit to generate KPATH.in
    ```shell
    vaspkit -task 303
    mv KPATH.in KPOINTS
    ```

* (III) MBJ band calculation based on step (II).
  * (a) PBE SCF calculation with zero weight k-points.
    * (1)Copy the IBZKPT at step (II-a) into KPOINTS
    * (2) Find all k-points from OUTCAR at step (II-b) and add to the KPOINTS with zero weight.
    * Be careful that you should copy the k-point 'k-points in reciprocal lattice and weights' instead of 'k-points in units of 2pi/SCALE and weight' in OUTCAR
    ### INCAR
    ```shell
    ISTART=0
    ICHARG=2
    ```

  * (b) MBJ SCF calculation with zero weight k-points base on (III-a)
  ### INCAR
  ```shell
  ISTART=1
  ICHARG=0
  
  ###MBJ:
  METAGGA=MBJ
  LASPH=.TRUE.
  #CMBJ=XXX(1.3)
  ```
  
  * (c) Post-processing for band ploting
    * Copy the Line-Mode KPOINTS from (II-b)
    * Delete the k points with weight in EIGENVAL
    * Ploting 
    ```shell
    vaspkit -task 211
    python band.py
    ```
  
  
