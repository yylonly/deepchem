#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 00:07:10 2017

@author: zqwu
"""
import deepchem

hps = {}
hps['tf'] = {
    'layer_sizes': [1500],
    'weight_init_stddevs': [0.02],
    'bias_init_consts': [1.],
    'dropouts': [0.5],
    'penalty': 0.1,
    'penalty_type': 'l2',
    'batch_size': 50,
    'nb_epoch': 10,
    'learning_rate': 0.001
}

hps['tf_robust'] = {
    'layer_sizes': [1500],
    'weight_init_stddevs': [0.02],
    'bias_init_consts': [1.],
    'dropouts': [0.5],
    'bypass_layer_sizes': [200],
    'bypass_weight_init_stddevs': [0.02],
    'bypass_bias_init_consts': [1.],
    'bypass_dropouts': [0.5],
    'penalty': 0.1,
    'penalty_type': 'l2',
    'batch_size': 50,
    'nb_epoch': 10,
    'learning_rate': 0.0005
}
hps['logreg'] = {
    'penalty': 0.1,
    'penalty_type': 'l2',
    'batch_size': 50,
    'nb_epoch': 10,
    'learning_rate': 0.005
}
hps['irv'] = {
    'penalty': 0.,
    'penalty_type': 'l2',
    'batch_size': 50,
    'nb_epoch': 10,
    'learning_rate': 0.001,
    'n_K': 10
}
hps['graphconv'] = {
    'batch_size': 50,
    'nb_epoch': 15,
    'learning_rate': 0.0005,
    'n_filters': 64,
    'n_fully_connected_nodes': 128,
    'seed': 123
}
hps['dag'] = {
    'batch_size': 64,
    'nb_epoch': 50,
    'learning_rate': 0.001,
    'n_graph_feat': 30,
    'seed': 123
}
hps['weave'] = {
    'batch_size': 64,
    'nb_epoch': 40,
    'learning_rate': 0.001,
    'n_graph_feat': 128,
    'n_pair_feat': 14,
    'seed': 123
}
hps['rf'] = {'n_estimators': 500}
hps['xgb'] = {
    'max_depth': 5,
    'learning_rate': 0.05,
    'n_estimators': 3000,
    'gamma': 0,
    'min_child_weight': 5,
    'max_delta_step': 1,
    'subsample': 0.53,
    'colsample_bytree': 0.66,
    'colsample_bylevel': 1,
    'reg_alpha': 0,
    'reg_lambda': 1,
    'scale_pos_weight': 1,
    'base_score': 0.5,
    'seed': 2016,
    'early_stopping_rounds': 100
}

hps['tf_regression'] = {
    'layer_sizes': [1000, 1000],
    'weight_init_stddevs': [0.02, 0.02],
    'bias_init_consts': [1., 1.],
    'dropouts': [0.25, 0.25],
    'penalty': 0.0005,
    'penalty_type': 'l2',
    'batch_size': 128,
    'nb_epoch': 50,
    'learning_rate': 0.0008
}
hps['tf_regression_ft'] = {
    'layer_sizes': [400, 100, 100],
    'weight_init_stddevs': [0.05, 0.1, 0.1],
    'bias_init_consts': [0., 0., 0.],
    'dropouts': [0.01, 0.01, 0.01],
    'penalty': 0.,
    'penalty_type': 'l2',
    'batch_size': 25,
    'nb_epoch': 50,
    'learning_rate': 0.001,
    'fit_transformers': deepchem.trans.CoulombFitTransformer
}
hps['rf_regression'] = {'n_estimators': 500}
hps['graphconvreg'] = {
    'batch_size': 128,
    'nb_epoch': 20,
    'learning_rate': 0.0005,
    'n_filters': 128,
    'n_fully_connected_nodes': 256,
    'seed': 123
}
hps['dtnn'] = {
    'batch_size': 64,
    'nb_epoch': 50,
    'learning_rate': 0.0005,
    'n_embedding': 20,
    'n_distance': 100,
    'seed': 123
}
hps['dag_regression'] = {
    'batch_size': 64,
    'nb_epoch': 50,
    'learning_rate': 0.001,
    'n_graph_feat': 30,
    'seed': 123
}
hps['weave_regression'] = {
    'batch_size': 64,
    'nb_epoch': 50,
    'learning_rate': 0.001,
    'n_graph_feat': 128,
    'n_pair_feat': 14,
    'seed': 123
}
hps['xgb_regression'] = {
    'max_depth': 5,
    'learning_rate': 0.05,
    'n_estimators': 3000,
    'gamma': 0,
    'min_child_weight': 5,
    'max_delta_step': 1,
    'subsample': 0.53,
    'colsample_bytree': 0.66,
    'colsample_bylevel': 1,
    'reg_alpha': 0,
    'reg_lambda': 1,
    'scale_pos_weight': 1,
    'base_score': 0.5,
    'seed': 2016,
    'early_stopping_rounds': 100
}

hps['siamese'] = {
    'n_pos': 1,
    'n_neg': 1,
    'test_batch_size': 128,
    'n_filters': [64, 128, 64],
    'n_fully_connected_nodes': [128],
    'nb_epochs': 1,
    'n_train_trials': 2000,
    'n_eval_trials': 20,
    'learning_rate': 1e-4
}
hps['res'] = {
    'n_pos': 1,
    'n_neg': 1,
    'test_batch_size': 128,
    'n_filters': [64, 128, 64],
    'n_fully_connected_nodes': [128],
    'max_depth': 3,
    'nb_epochs': 1,
    'n_train_trials': 2000,
    'n_eval_trials': 20,
    'learning_rate': 1e-4
}
hps['attn'] = {
    'n_pos': 1,
    'n_neg': 1,
    'test_batch_size': 128,
    'n_filters': [64, 128, 64],
    'n_fully_connected_nodes': [128],
    'max_depth': 3,
    'nb_epochs': 1,
    'n_train_trials': 2000,
    'n_eval_trials': 20,
    'learning_rate': 1e-4
}
