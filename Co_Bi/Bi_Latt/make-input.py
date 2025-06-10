from ase.build import bulk, surface, add_vacuum, hcp0001
from dlePy.qe.pwscf import PWscfInput, write_pwscf_input, update_keyword

Latt_Values = [2.30, 2.31, 2.32, 2.33, 2.34,2.35, 2.36, 2.37, 2.38, 2.39, 2.40, 2.41, 2.42]

for latt_param in Latt_Values:

    #create Cobalt bi-layer
    a = latt_param
    c = a*1.62753
    Cobulk = bulk( 'Co', 'hcp', a=a, c = c)
    bi = hcp0001('Co', size = (1,1,2), a=a, c=c, vacuum = 7.5,orthogonal = False, periodic = False)

    

    # Create `pwscf` object for `bi`
    pwscf = PWscfInput ( bi )

    #Change the calculation to scf
    update_keyword( pwscf.control.settings, 'calculation', 'scf' )

    update_keyword( pwscf.control.settings, 'pseudo_dir', '/shared/ESPRESSO/PSLIBRARY/1.0.0/pbe/PSEUDOPOTENTIALS/' )

    update_keyword( pwscf.control.settings, 'prefix', 'scf' )
    update_keyword( pwscf.control.io, 'disk_io', 'default')
    update_keyword( pwscf.control.io,'wf_collect',False)

    mass = [ 58.933195 ]
    pseudo_potential = [ 'Co.pbe-n-kjpaw_psl.1.0.0.UPF' ]
    update_keyword( pwscf.atomic_species, 'mass', mass )
    update_keyword( pwscf.atomic_species, 'pseudo_potential', pseudo_potential )

    update_keyword( pwscf.system.occupations,'degauss', 0.007)
    update_keyword( pwscf.system.occupations,'smearing','fd')


    update_keyword( pwscf.kpoints, 'mesh', [10,10,1] )
    update_keyword( pwscf.kpoints, 'smesh',[0,0,0] )

    update_keyword( pwscf.system.ecut, 'ecutwfc', 65.0)
    update_keyword( pwscf.system.ecut, 'ecutrho', 4*65.0)
    
    #Convert to string for input file
    latt_str = f"{a:.2f}"
    out_filename = f"scf_{latt_str}.inp"
    write_pwscf_input( pwscf, out_filename)
