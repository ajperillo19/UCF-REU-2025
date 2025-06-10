from ase.build import bulk, surface, add_vacuum, hcp0001
from dlePy.qe.pwscf import PWscfInput, write_pwscf_input, update_keyword

KP_Values = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

for kp in KP_Values:

    #create Cobalt monolayer
    latt = 2.45
    c = latt*1.62753
    Cobulk = bulk( 'Co', 'hcp', a = latt, c = c)
    mono = hcp0001('Co', size = (1,1,1),  a=latt, c=c, vacuum = 7.5,orthogonal = False, periodic = False)

    

    # Create `pwscf` object for `mono`
    pwscf = PWscfInput ( mono )

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


    update_keyword( pwscf.kpoints, 'mesh', [kp,kp,1] )
    update_keyword( pwscf.kpoints, 'smesh',[0,0,0] )

    update_keyword( pwscf.system.ecut, 'ecutwfc', 65.0)
    update_keyword( pwscf.system.ecut, 'ecutrho', 4*65.0)
    
    #Convert to string for input file
    kp_str = f"{kp:02d}"
    out_filename = f"scf_kp_{kp_str}.inp"
    write_pwscf_input( pwscf, out_filename)
