from dlePy.qe.pwscf import PWscfInput, write_pwscf_input, update_keyword
import ase.build
from ase.build import mx2
from ase.visualize import view
from ase import Atoms

Latt_Values = [3.12, 3.13, 3.14, 3.15, 3.16, 3.17, 3.18, 3.19, 3.20, 3.21, 3.22, 3.23, 3.24]

for a in Latt_Values:



    Mo_S2 = mx2(formula = 'MoS2', kind = '2H', a = a, thickness = 3.19, size = (1,1,1), vacuum = 6.15)
    

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


    update_keyword( pwscf.kpoints, 'mesh', [8,8,1] )
    update_keyword( pwscf.kpoints, 'smesh',[0,0,0] )

    update_keyword( pwscf.system.structure, 'nat', 3)
    update_keyword( pwscf.system.structure, 'ntyp', 2)
    update_keyword( pwscf.system.ecut, 'ecutwfc', 80.0)
    update_keyword( pwscf.system.ecut, 'ecutrho', 4*80.0)
    
    #Convert to string for input file
    latt_str = f"{a:.02f}"
    out_filename = f"scf_A_{latt_str}.inp"
    write_pwscf_input( pwscf, out_filename)
