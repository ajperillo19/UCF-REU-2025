from ase.build import bulk, surface, add_vacuum, hcp0001
from dlePy.qe.pwscf import PWscfInput, write_pwscf_input, update_keyword

Cut_Values = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

for ecut in Cut_Values:

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


    update_keyword( pwscf.kpoints, 'mesh', [16,16,1] )
    update_keyword( pwscf.kpoints, 'smesh',[0,0,0] )

    update_keyword( pwscf.system.ecut, 'ecutwfc', ecut)
    update_keyword( pwscf.system.ecut, 'ecutrho', 4*ecut)
    
    #Convert to string for input file
    ecut_str = f"{ecut:02d}"
    out_filename = f"scf_{ecut_str}.inp"
    write_pwscf_input( pwscf, out_filename)
