from dlePy.qe.pwscf import PWscfInput, write_pwscf_input, update_keyword
import ase.build
from ase.build import mx2
from ase.visualize import view
from ase import Atoms

Cut_Values = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

for ecut in Cut_Values:



    Mo_S2 = mx2(formula = 'MoS2', kind = '2H', a = 3.18, thickness = 3.19, size = (1,1,1), vacuum = 6.15)
    

    # Create `pwscf` object for `Mo_S2`
    pwscf = PWscfInput ( Mo_S2 )

    #Change the calculation to scf
    update_keyword( pwscf.control.settings, 'calculation', 'scf' )

    update_keyword( pwscf.control.settings, 'pseudo_dir', '/shared/ESPRESSO/PSLIBRARY/1.0.0/pbe/PSEUDOPOTENTIALS/' )

    update_keyword( pwscf.control.settings, 'prefix', 'scf' )
    update_keyword( pwscf.control.io, 'disk_io', 'default')
    update_keyword( pwscf.control.io,'wf_collect',False)

    mass_Mo = 95.94 
    pseudo_potential_Mo = 'Mo.pbe-spn-kjpaw_psl.1.0.0.UPF'
    mass_S =  32.065
    pseudo_potential_S = 'S.pbe-n-kjpaw_psl.1.0.0.UPF'

    update_keyword( pwscf.atomic_species, 'mass', [mass_Mo, mass_S] )
    update_keyword( pwscf.atomic_species, 'pseudo_potential', [pseudo_potential_Mo, pseudo_potential_S] )

    update_keyword( pwscf.system.occupations,'degauss', 0.007)
    update_keyword( pwscf.system.occupations,'smearing','fd')


    update_keyword( pwscf.kpoints, 'mesh', [16,16,1] )
    update_keyword( pwscf.kpoints, 'smesh',[0,0,0] )

    update_keyword( pwscf.system.structure, 'nat', 3)
    update_keyword( pwscf.system.structure, 'ntyp', 2)
    update_keyword( pwscf.system.ecut, 'ecutwfc', ecut)
    update_keyword( pwscf.system.ecut, 'ecutrho', 4*ecut)
    
    #Convert to string for input file
    ecut_str = f"{ecut:02d}"
    out_filename = f"scf_{ecut_str}.inp"
    write_pwscf_input( pwscf, out_filename)
