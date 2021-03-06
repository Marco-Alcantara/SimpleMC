##
# This class has parameter definitions for all
# parameters used in this code.
##
# Change here for bounds, or import and rewrite.
##
##


from .Parameter import Parameter

# Parameters are value, variation, bounds
Om_par   = Parameter("Om",   0.3038,  0.05,    (0.05, 0.5),   "\Omega_m")
Obh2_par = Parameter("Obh2", 0.02234, 0.001, (0.02, 0.025), "\Omega_{b}h^2")
h_par    = Parameter("h",    0.6821,  0.05,   (0.4, 1.0),    "h")

mnu_par  = Parameter("mnu",  0.06,    0.1,    (0, 1.0),      "\Sigma m_{\\nu}")
Nnu_par  = Parameter("Nnu",  3.046,   0.5,    (3.046, 5.046),"N_{\\rm eff}")

Ok_par = Parameter("Ok", 0.0, 0.01, (-0.1, 0.1), "\Omega_k")
w_par  = Parameter("w", -1., 0.1, (-2.0, 0.0), "w_0")
wa_par = Parameter("wa", 0.0, 0.1, (-2.0, 2.0), "w_a")

s8_par    = Parameter("s8", 0.8, 0.01, (0.6, 1.0), "s8")

# this is the prefactor parameter c/rdH0
Pr_par = Parameter("Pr", 28.6, 4, (5, 70), "c/(H_0r_d)")

# Poly Cosmology Parameters
Om1_par = Parameter("Om1", 0.0, 0.7, (-3, 3), "\Omega_1")
Om2_par = Parameter("Om2", 0.0, 0.7, (-3, 3), "\Omega_2")

# JordiCDM Cosmology Parameters
q_par  = Parameter("q",  0.0, 0.2, (0, 1),      "q")
za_par = Parameter("za", 3,   1.0, (2, 10),     "z_a")
zb_par = Parameter("zb", 1,   0.5, (0, 2),      "z_b")
wd_par = Parameter("wd", -1,  0.5, (-2.0, 0.0), "w_d")
Od_par = Parameter("Od", 0.0, 0.2, (0.0, 1.0),  "O_d")

# Weird model
mu_par  = Parameter("mu",  2.13,    0.1,  (0.01, 5), "\mu")
Amp_par = Parameter("Amp", -0.1839, 0.01, (-2, 2),   "Amp")
sig_par = Parameter("sig", 0.1,     0.2,  (0, 3.0),  "\sig")

# Tired Light
beta_par = Parameter("beta", 1, 0.1, (-1, 1), "\\beta")

# Spline reconstruction
Sp1_par = Parameter("Sp1", 1, 0.01, (-1.2, 1.2), "S1")
Sp2_par = Parameter("Sp2", 1, 0.01, (-1.2, 1.2), "S2")
Sp3_par = Parameter("Sp3", 1, 0.01, (-1.2, 1.2), "S3")
Sp4_par = Parameter("Sp4", 1, 0.01, (-1.2, 1.2), "S4")


# Step-wise dark energy density (edit: JG)
# number of redshift boundaries (fixed)
step_nz_par = Parameter("StepNZ", 3, 1, (0., 10.), "nz")
# redshift of bin boundaries (fixed)
step_z0_par = Parameter("StepZ0", 0.5, 0.01, (0., 10.), "z0")
step_z1_par = Parameter("StepZ1", 1.0, 0.01, (0., 10.), "z1")
step_z2_par = Parameter("StepZ2", 1.6, 0.01, (0., 10.), "z2")
step_z3_par = None
step_z4_par = None

# rho_DE/rho_c in redshift bins (nz+1, free), 0.2 is working
step_rho0_par = Parameter("StepR0", 0.7, 0.5, (-20., 20.), "\\rho_0")
step_rho1_par = Parameter("StepR1", 0.7, 0.5, (-20., 20.), "\\rho_1")
step_rho2_par = Parameter("StepR2", 0.7, 0.5, (-20., 20.), "\\rho_2")
step_rho3_par = Parameter("StepR3", 0.7, 0.5, (-20., 20.), "\\rho_3")
step_rho4_par = None
step_rho5_par = None

# Decaying Dark Matter
lambda_par = Parameter("lambda", 1.0, 1.0, (0., 20.0), "\lambda")
xfrac_par  = Parameter("xfrac",  0.1, 0.1, (0.0, 1.0), "f_x")

# Early Dark Energy
Ode_par = Parameter("Ode", 0.05, 0.01, (0, 0.9), "\Omega^e_{\\rm de}")

# Slow-Roll DE
dw_par = Parameter("dw", 0, 0.1, (-1.0, 1.0), "\delta w_0")

# QuinDE
lam_par = Parameter("lam", 1,  0.5, (0, 5),      "\lambda")
V0_par  = Parameter("V0",  1,  1,   (0, 30),     "V_0")
A_par   = Parameter("A",   10,  1,  (-20, 20),   "A")
B_par   = Parameter("B",   -20, 2,  (-100, 100), "B")

# wDark Matter
wDM_par = Parameter("wDM", 0.0, 0.1, (-1.0, 1.0), "w_{DM}")

#Generic models
a_par = Parameter("a", 0., 0.5, (-10., 10.), "a" )
b_par = Parameter("b", 0., 0.5, (-10., 10.), "b")


#Compress data
#plus the first bin that is fix
Nbins = 15
step  = (13-1.3)/(Nbins-1)
zbin_par = [Parameter("zbin%d"%i, 1.3+step*i, 0.3, (step*i, 3+step*i), "zbin%d"%i) for i in range(Nbins)]


#Quintess Cosmology
mphi_par   = Parameter("mphi", 0.2, 0.1, (-5, 1), "m_{\phi}")

#PhiRatra
alpha_par  = Parameter("alpha", 0.01, 0.005, (0.001, 0.05), "\\alpha")

#Quintom Cosology
mquin_par  = Parameter("mquin", 1.2, 0.1, (0, 4), "m_{\phi}")
mphan_par  = Parameter("mphan", 0.7 , 0.1, (0, 2), "m_{\psi}")
beta2_par  = Parameter("beta",  1.0, 0.5, (0, 20), "\\beta")
iniphi_par = Parameter("iniphi", 1.0, 0.1, (0, 2), "\phi_0")

#Phi Cosmology
phialp_par  = Parameter("phialp",   1.0, 0.1,  (-3, 3.), "\\alpha")
philam_par  = Parameter("philam",   0.5, 0.01, (-2.0, 2.0), "\\lambda_i")
phibeta_par = Parameter("phibeta",  0.0, 0.05, (-3.0, 3.0), "\\beta")
phimu_par   = Parameter("phimu",    1.0, 0.05, (-4.0, 4.0), "\\mu")

#QDGP
Oq_par = Parameter("Oq",  0.7, 0.05, (0.5, 1.0), "\Omega_q")
wq_par = Parameter("wq",  -0.9, 0.05, (-1.0, -0.5), "w_q")

#Rotation
Anfw_par = Parameter("Anfw",  0.1, 0.01, (0.0, 0.5), "A_s")
rs_par =   Parameter("rs",  400., 10.0, (0.0, 600.0), "r_s")