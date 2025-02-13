import argparse

parser = argparse.ArgumentParser()

# optimizer
parser.add_argument('--gpu_id', type=str, default='0', help='train use gpu')
parser.add_argument('--lr_mode', type=str, default="poly")
parser.add_argument('--base_lr', type=float, default=1e-4)
parser.add_argument('--finetune_lr', type=float, default=1e-4)
parser.add_argument('--decay_rate', type=float, default=0.1, help='decay rate of learning rate')
parser.add_argument('--decay_epoch', type=int, default=50, help='every n epochs decay learning rate')
parser.add_argument('--clip', type=float, default=0.5, help='gradient clipping margin')

# train schedule
parser.add_argument('--pretrain_epoches', type=int, default=100)
parser.add_argument('--finetune_epoches', type=int, default=1)
parser.add_argument('--log_inteval', type=int, default=50)

# data
parser.add_argument('--data_statistics', type=str,
                    default="dataset/statistics.pth")
parser.add_argument('--img_dataset_list', type=str,
                    default=["IVPS-TrainSet"])
parser.add_argument('--video_dataset_list', type=str,
                    default=["ASU-Mayo_Clinic", "CVC-ClinicDB-612", "CVC-ColonDB-300"])
parser.add_argument('--img_dataset_root', type=str,
                    default="dataset/")
parser.add_argument('--video_dataset_root', type=str,
                    default="dataset/VPS-TrainSet/")
parser.add_argument('--size', type=tuple,
                    default=(256, 448))
parser.add_argument('--pretrain_batchsize', type=int, default=20)
parser.add_argument('--video_batchsize', type=int, default=4)
parser.add_argument('--video_time_clips', type=int, default=5)
parser.add_argument('--video_testset_root', type=str, default="dataset/VPS-TestSet/")

# pretrain
parser.add_argument('--pretrain_state_dict', type=str, default="lib/statedict/PNS_Pretrain.pth")
parser.add_argument('--save_path', type=str, default='snapshot/PNS/')
config = parser.parse_args()
