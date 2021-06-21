import math

seed = 0

THRESHOLD_POSITIVE = 0.1
THRESHOLD_NEGATIVE = 0

threshold_point = 25
window = 120

sigma = 18.5
sigma_aff = 20

boundary_character = math.exp(-1/2*(threshold_point**2)/(sigma**2))
boundary_affinity = math.exp(-1/2*(threshold_point**2)/(sigma_aff**2))

threshold_character = boundary_character + 0.03
threshold_affinity = boundary_affinity + 0.03

threshold_character_upper = boundary_character + 0.2
threshold_affinity_upper = boundary_affinity + 0.2

scale_character = math.sqrt(math.log(boundary_character)/math.log(threshold_character_upper))
scale_affinity = math.sqrt(math.log(boundary_affinity)/math.log(threshold_affinity_upper))

dataset_name = 'ICDAR2013_ICDAR2017'
test_dataset_name = 'ICDAR2013'

print(
	'Boundary character value = ', boundary_character,
	'| Threshold character value = ', threshold_character,
	'| Threshold character upper value = ', threshold_character_upper
)
print(
	'Boundary affinity value = ', boundary_affinity,
	'| Threshold affinity value = ', threshold_affinity,
	'| Threshold affinity upper value = ', threshold_affinity_upper
)
print('Scale character value = ', scale_character, '| Scale affinity value = ', scale_affinity)
print('Training Dataset = ', dataset_name, '| Testing Dataset = ', test_dataset_name)

DataLoaderSYNTH_base_path = '/home/greg/dev/datasets/ICDAR2015-Text/ICDAR2015_Incidental/train'
DataLoaderSYNTH_mat = '/home/greg/dev/datasets/Synth/SynthText/gt.mat'
DataLoaderSYNTH_Train_Synthesis = '/home/greg/dev/datasets/ICDAR2015-Text/ICDAR2015_Incidental/train'

DataLoader_Other_Synthesis = '/home/greg/dev/datasets/Synth/'+dataset_name+'/Save/'
Other_Dataset_Path = '/home/greg/dev/datasets/Synth/'+dataset_name

save_path = '/home/greg/dev/datasets/Synth/Models/WeakSupervision/'+dataset_name
images_path = '/home/greg/dev/datasets/Synth/'+dataset_name+'/Images'
target_path = '/home/greg/dev/datasets/Synth/'+dataset_name+'/Generated'

Test_Dataset_Path = '/home/greg/dev/datasets/Synth/'+test_dataset_name

threshold_word = 0.7
threshold_fscore = 0.5

dataset_pre_process = {
	'ic13': {
		'train': {
			'target_json_path': '/home/greg/dev/datasets/ICDAR2015-Text/target_json',
			'target_folder_path': '/home/greg/dev/datasets/ICDAR2015-Text/target_json',
		},
		'test': {
			'target_json_path': '/home/greg/dev/datasets/ICDAR2015-Text/target_json',
			'target_folder_path': '/home/greg/dev/datasets/ICDAR2015-Text/target_json',
		}
	},
	'ic15': {
		'train': {
			'target_json_path': '/home/greg/dev/datasets/ICDAR2015-Text/ICDAR2015_Incidental/train',
			'target_folder_path': '/home/greg/dev/datasets/ICDAR2015-Text/ICDAR2015_Incidental/train',
		},
		'test': {
			'target_json_path': '/home/greg/dev/datasets/ICDAR2015-Text/ICDAR2015_Incidental/test',
			'target_folder_path': '/home/greg/dev/datasets/ICDAR2015-Text/ICDAR2015_Incidental/test',
		}
	}
}

start_iteration = 0
skip_iterations = []
