class Hparams:
    class Audio:
        num_mels = 80 # 梅尔谱维度
        ppg_dim = 351 # PPG的向量维度
        bn_dim = 256 # BNF的向量维度
        num_freq = 1025  # 频率维度
        min_mel_freq = 30. # 最小梅尔谱频率
        max_mel_freq = 7600. # 最大梅尔谱频率
        sample_rate = 16000 # 采样率
        frame_length_ms = 25 # 窗长
        frame_shift_ms = 10 # 窗移
        upper_f0 = 500. # 最高基音频率
        lower_f0 = 30. # 最低基音频率
        n_mfcc = 13 # MFCC的采样帧长
        preemphasize = 0.97
        min_level_db = -80.0
        ref_level_db = 20.0
        max_abs_value = 1.
        symmetric_specs = False
        griffin_lim_iters = 60
        power = 1.5
        center = True

    class SPEAKERS:
        num_spk = 3
        spk_to_inds = ['bzn', 'mst-female', 'mst-male']

    class TrainToOne:
        dev_set_rate = 0.1
        test_set_rate = 0.05
        epochs = 60
        train_batch_size = 32
        test_batch_size = 1
        shuffle_buffer = 128
        shuffle = True
        learning_rate = 1e-3
        num_workers = 16

    class TrainToMany:
        dev_set_rate = 0.1
        test_set_rate = 0.05
        epochs = 60
        train_batch_size = 32
        test_batch_size = 1
        shuffle_buffer = 128
        shuffle = True
        learning_rate = 1e-3
        num_workers = 16

    class BLSTMConversionModel:
        lstm_hidden = 256

    class BLSTMToManyConversionModel:
        lstm_hidden = 256
        spk_embd_dim = 64
