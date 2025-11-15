"""
Audio Spectrum Visualization Modes 701-750
Tech & Digital Category (Part 1)
"""
from .base import BaseModeVisualizer
import numpy as np
import cv2


class Modes701_750(BaseModeVisualizer):
    """Visualization modes 701 through 750 - Tech & Digital"""

    def __init__(self, visualizer):
        super().__init__(visualizer)

    def draw_mode_701_binary_rain(self, frame, magnitudes):
        """Mode 701: Binary rain visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_702_hexadecimal_grid(self, frame, magnitudes):
        """Mode 702: Hexadecimal grid visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_703_circuit_board(self, frame, magnitudes):
        """Mode 703: Circuit board visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_704_data_flow(self, frame, magnitudes):
        """Mode 704: Data flow visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_705_packet_transmission(self, frame, magnitudes):
        """Mode 705: Packet transmission visualization"""
        spacing = 40
        for y in range(0, self.height, spacing):
            for x in range(0, self.width, spacing):
                idx = ((y // spacing) * 20 + x // spacing) % len(magnitudes)
                mag = magnitudes[idx]
                if mag > 0.3:
                    brightness = int(100 + mag * 155)
                    cv2.rectangle(frame, (x, y), (x + int(mag * 30), y + int(mag * 30)),
                                (0, brightness, brightness), -1)
        return frame

    def draw_mode_706_network_topology(self, frame, magnitudes):
        """Mode 706: Network topology visualization"""
        bass = self.get_bass(magnitudes)
        for i in range(20):
            y = int((i / 20) * self.height)
            progress = int(bass * self.width)
            cv2.line(frame, (0, y), (progress, y), (0, 255, int(100 + i * 5)), 2)
            if i % 4 == 0:
                cv2.circle(frame, (progress, y), 5, (0, 255, 255), -1)
        return frame

    def draw_mode_707_server_cluster(self, frame, magnitudes):
        """Mode 707: Server cluster visualization"""
        bass = self.get_bass(magnitudes)
        for i in range(20):
            y = int((i / 20) * self.height)
            progress = int(bass * self.width)
            cv2.line(frame, (0, y), (progress, y), (0, 255, int(100 + i * 5)), 2)
            if i % 4 == 0:
                cv2.circle(frame, (progress, y), 5, (0, 255, 255), -1)
        return frame

    def draw_mode_708_cloud_computing(self, frame, magnitudes):
        """Mode 708: Cloud computing visualization"""
        bass = self.get_bass(magnitudes)
        for i in range(20):
            y = int((i / 20) * self.height)
            progress = int(bass * self.width)
            cv2.line(frame, (0, y), (progress, y), (0, 255, int(100 + i * 5)), 2)
            if i % 4 == 0:
                cv2.circle(frame, (progress, y), 5, (0, 255, 255), -1)
        return frame

    def draw_mode_709_distributed_system(self, frame, magnitudes):
        """Mode 709: Distributed system visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_710_peer_to_peer(self, frame, magnitudes):
        """Mode 710: Peer-to-peer visualization"""
        bass = self.get_bass(magnitudes)
        for i in range(20):
            y = int((i / 20) * self.height)
            progress = int(bass * self.width)
            cv2.line(frame, (0, y), (progress, y), (0, 255, int(100 + i * 5)), 2)
            if i % 4 == 0:
                cv2.circle(frame, (progress, y), 5, (0, 255, 255), -1)
        return frame

    def draw_mode_711_blockchain(self, frame, magnitudes):
        """Mode 711: Blockchain visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_712_hash_function(self, frame, magnitudes):
        """Mode 712: Hash function visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_713_encryption(self, frame, magnitudes):
        """Mode 713: Encryption visualization"""
        bass = self.get_bass(magnitudes)
        for i in range(20):
            y = int((i / 20) * self.height)
            progress = int(bass * self.width)
            cv2.line(frame, (0, y), (progress, y), (0, 255, int(100 + i * 5)), 2)
            if i % 4 == 0:
                cv2.circle(frame, (progress, y), 5, (0, 255, 255), -1)
        return frame

    def draw_mode_714_public_key(self, frame, magnitudes):
        """Mode 714: Public key visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_715_digital_signature(self, frame, magnitudes):
        """Mode 715: Digital signature visualization"""
        bass = self.get_bass(magnitudes)
        for i in range(20):
            y = int((i / 20) * self.height)
            progress = int(bass * self.width)
            cv2.line(frame, (0, y), (progress, y), (0, 255, int(100 + i * 5)), 2)
            if i % 4 == 0:
                cv2.circle(frame, (progress, y), 5, (0, 255, 255), -1)
        return frame

    def draw_mode_716_zero_knowledge_proof(self, frame, magnitudes):
        """Mode 716: Zero knowledge proof visualization"""
        bass = self.get_bass(magnitudes)
        for i in range(20):
            y = int((i / 20) * self.height)
            progress = int(bass * self.width)
            cv2.line(frame, (0, y), (progress, y), (0, 255, int(100 + i * 5)), 2)
            if i % 4 == 0:
                cv2.circle(frame, (progress, y), 5, (0, 255, 255), -1)
        return frame

    def draw_mode_717_homomorphic_encryption(self, frame, magnitudes):
        """Mode 717: Homomorphic encryption visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_718_secure_multiparty_computation(self, frame, magnitudes):
        """Mode 718: Secure multiparty computation visualization"""
        spacing = 40
        for y in range(0, self.height, spacing):
            for x in range(0, self.width, spacing):
                idx = ((y // spacing) * 20 + x // spacing) % len(magnitudes)
                mag = magnitudes[idx]
                if mag > 0.3:
                    brightness = int(100 + mag * 155)
                    cv2.rectangle(frame, (x, y), (x + int(mag * 30), y + int(mag * 30)),
                                (0, brightness, brightness), -1)
        return frame

    def draw_mode_719_differential_privacy(self, frame, magnitudes):
        """Mode 719: Differential privacy visualization"""
        spacing = 40
        for y in range(0, self.height, spacing):
            for x in range(0, self.width, spacing):
                idx = ((y // spacing) * 20 + x // spacing) % len(magnitudes)
                mag = magnitudes[idx]
                if mag > 0.3:
                    brightness = int(100 + mag * 155)
                    cv2.rectangle(frame, (x, y), (x + int(mag * 30), y + int(mag * 30)),
                                (0, brightness, brightness), -1)
        return frame

    def draw_mode_720_federated_learning(self, frame, magnitudes):
        """Mode 720: Federated learning visualization"""
        bass = self.get_bass(magnitudes)
        for i in range(20):
            y = int((i / 20) * self.height)
            progress = int(bass * self.width)
            cv2.line(frame, (0, y), (progress, y), (0, 255, int(100 + i * 5)), 2)
            if i % 4 == 0:
                cv2.circle(frame, (progress, y), 5, (0, 255, 255), -1)
        return frame

    def draw_mode_721_neural_network(self, frame, magnitudes):
        """Mode 721: Neural network visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_722_deep_learning(self, frame, magnitudes):
        """Mode 722: Deep learning visualization"""
        bass = self.get_bass(magnitudes)
        for i in range(20):
            y = int((i / 20) * self.height)
            progress = int(bass * self.width)
            cv2.line(frame, (0, y), (progress, y), (0, 255, int(100 + i * 5)), 2)
            if i % 4 == 0:
                cv2.circle(frame, (progress, y), 5, (0, 255, 255), -1)
        return frame

    def draw_mode_723_convolutional_layer(self, frame, magnitudes):
        """Mode 723: Convolutional layer visualization"""
        spacing = 40
        for y in range(0, self.height, spacing):
            for x in range(0, self.width, spacing):
                idx = ((y // spacing) * 20 + x // spacing) % len(magnitudes)
                mag = magnitudes[idx]
                if mag > 0.3:
                    brightness = int(100 + mag * 155)
                    cv2.rectangle(frame, (x, y), (x + int(mag * 30), y + int(mag * 30)),
                                (0, brightness, brightness), -1)
        return frame

    def draw_mode_724_recurrent_connection(self, frame, magnitudes):
        """Mode 724: Recurrent connection visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_725_attention_mechanism(self, frame, magnitudes):
        """Mode 725: Attention mechanism visualization"""
        bass = self.get_bass(magnitudes)
        for i in range(20):
            y = int((i / 20) * self.height)
            progress = int(bass * self.width)
            cv2.line(frame, (0, y), (progress, y), (0, 255, int(100 + i * 5)), 2)
            if i % 4 == 0:
                cv2.circle(frame, (progress, y), 5, (0, 255, 255), -1)
        return frame

    def draw_mode_726_transformer_architecture(self, frame, magnitudes):
        """Mode 726: Transformer architecture visualization"""
        spacing = 40
        for y in range(0, self.height, spacing):
            for x in range(0, self.width, spacing):
                idx = ((y // spacing) * 20 + x // spacing) % len(magnitudes)
                mag = magnitudes[idx]
                if mag > 0.3:
                    brightness = int(100 + mag * 155)
                    cv2.rectangle(frame, (x, y), (x + int(mag * 30), y + int(mag * 30)),
                                (0, brightness, brightness), -1)
        return frame

    def draw_mode_727_residual_connection(self, frame, magnitudes):
        """Mode 727: Residual connection visualization"""
        spacing = 40
        for y in range(0, self.height, spacing):
            for x in range(0, self.width, spacing):
                idx = ((y // spacing) * 20 + x // spacing) % len(magnitudes)
                mag = magnitudes[idx]
                if mag > 0.3:
                    brightness = int(100 + mag * 155)
                    cv2.rectangle(frame, (x, y), (x + int(mag * 30), y + int(mag * 30)),
                                (0, brightness, brightness), -1)
        return frame

    def draw_mode_728_skip_connection(self, frame, magnitudes):
        """Mode 728: Skip connection visualization"""
        spacing = 40
        for y in range(0, self.height, spacing):
            for x in range(0, self.width, spacing):
                idx = ((y // spacing) * 20 + x // spacing) % len(magnitudes)
                mag = magnitudes[idx]
                if mag > 0.3:
                    brightness = int(100 + mag * 155)
                    cv2.rectangle(frame, (x, y), (x + int(mag * 30), y + int(mag * 30)),
                                (0, brightness, brightness), -1)
        return frame

    def draw_mode_729_batch_normalization(self, frame, magnitudes):
        """Mode 729: Batch normalization visualization"""
        bass = self.get_bass(magnitudes)
        for i in range(20):
            y = int((i / 20) * self.height)
            progress = int(bass * self.width)
            cv2.line(frame, (0, y), (progress, y), (0, 255, int(100 + i * 5)), 2)
            if i % 4 == 0:
                cv2.circle(frame, (progress, y), 5, (0, 255, 255), -1)
        return frame

    def draw_mode_730_dropout_regularization(self, frame, magnitudes):
        """Mode 730: Dropout regularization visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_731_activation_function(self, frame, magnitudes):
        """Mode 731: Activation function visualization"""
        spacing = 40
        for y in range(0, self.height, spacing):
            for x in range(0, self.width, spacing):
                idx = ((y // spacing) * 20 + x // spacing) % len(magnitudes)
                mag = magnitudes[idx]
                if mag > 0.3:
                    brightness = int(100 + mag * 155)
                    cv2.rectangle(frame, (x, y), (x + int(mag * 30), y + int(mag * 30)),
                                (0, brightness, brightness), -1)
        return frame

    def draw_mode_732_gradient_descent(self, frame, magnitudes):
        """Mode 732: Gradient descent visualization"""
        bass = self.get_bass(magnitudes)
        for i in range(20):
            y = int((i / 20) * self.height)
            progress = int(bass * self.width)
            cv2.line(frame, (0, y), (progress, y), (0, 255, int(100 + i * 5)), 2)
            if i % 4 == 0:
                cv2.circle(frame, (progress, y), 5, (0, 255, 255), -1)
        return frame

    def draw_mode_733_backpropagation(self, frame, magnitudes):
        """Mode 733: Backpropagation visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_734_loss_landscape(self, frame, magnitudes):
        """Mode 734: Loss landscape visualization"""
        spacing = 40
        for y in range(0, self.height, spacing):
            for x in range(0, self.width, spacing):
                idx = ((y // spacing) * 20 + x // spacing) % len(magnitudes)
                mag = magnitudes[idx]
                if mag > 0.3:
                    brightness = int(100 + mag * 155)
                    cv2.rectangle(frame, (x, y), (x + int(mag * 30), y + int(mag * 30)),
                                (0, brightness, brightness), -1)
        return frame

    def draw_mode_735_optimizer_trajectory(self, frame, magnitudes):
        """Mode 735: Optimizer trajectory visualization"""
        bass = self.get_bass(magnitudes)
        for i in range(20):
            y = int((i / 20) * self.height)
            progress = int(bass * self.width)
            cv2.line(frame, (0, y), (progress, y), (0, 255, int(100 + i * 5)), 2)
            if i % 4 == 0:
                cv2.circle(frame, (progress, y), 5, (0, 255, 255), -1)
        return frame

    def draw_mode_736_learning_rate_schedule(self, frame, magnitudes):
        """Mode 736: Learning rate schedule visualization"""
        bass = self.get_bass(magnitudes)
        for i in range(20):
            y = int((i / 20) * self.height)
            progress = int(bass * self.width)
            cv2.line(frame, (0, y), (progress, y), (0, 255, int(100 + i * 5)), 2)
            if i % 4 == 0:
                cv2.circle(frame, (progress, y), 5, (0, 255, 255), -1)
        return frame

    def draw_mode_737_momentum(self, frame, magnitudes):
        """Mode 737: Momentum visualization"""
        spacing = 40
        for y in range(0, self.height, spacing):
            for x in range(0, self.width, spacing):
                idx = ((y // spacing) * 20 + x // spacing) % len(magnitudes)
                mag = magnitudes[idx]
                if mag > 0.3:
                    brightness = int(100 + mag * 155)
                    cv2.rectangle(frame, (x, y), (x + int(mag * 30), y + int(mag * 30)),
                                (0, brightness, brightness), -1)
        return frame

    def draw_mode_738_adaptive_learning(self, frame, magnitudes):
        """Mode 738: Adaptive learning visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_739_weight_decay(self, frame, magnitudes):
        """Mode 739: Weight decay visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_740_early_stopping(self, frame, magnitudes):
        """Mode 740: Early stopping visualization"""
        bass = self.get_bass(magnitudes)
        for i in range(20):
            y = int((i / 20) * self.height)
            progress = int(bass * self.width)
            cv2.line(frame, (0, y), (progress, y), (0, 255, int(100 + i * 5)), 2)
            if i % 4 == 0:
                cv2.circle(frame, (progress, y), 5, (0, 255, 255), -1)
        return frame

    def draw_mode_741_cross_validation(self, frame, magnitudes):
        """Mode 741: Cross validation visualization"""
        bass = self.get_bass(magnitudes)
        for i in range(20):
            y = int((i / 20) * self.height)
            progress = int(bass * self.width)
            cv2.line(frame, (0, y), (progress, y), (0, 255, int(100 + i * 5)), 2)
            if i % 4 == 0:
                cv2.circle(frame, (progress, y), 5, (0, 255, 255), -1)
        return frame

    def draw_mode_742_ensemble_method(self, frame, magnitudes):
        """Mode 742: Ensemble method visualization"""
        bass = self.get_bass(magnitudes)
        for i in range(20):
            y = int((i / 20) * self.height)
            progress = int(bass * self.width)
            cv2.line(frame, (0, y), (progress, y), (0, 255, int(100 + i * 5)), 2)
            if i % 4 == 0:
                cv2.circle(frame, (progress, y), 5, (0, 255, 255), -1)
        return frame

    def draw_mode_743_boosting(self, frame, magnitudes):
        """Mode 743: Boosting visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_744_bagging(self, frame, magnitudes):
        """Mode 744: Bagging visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_745_random_forest(self, frame, magnitudes):
        """Mode 745: Random forest visualization"""
        bass = self.get_bass(magnitudes)
        for i in range(20):
            y = int((i / 20) * self.height)
            progress = int(bass * self.width)
            cv2.line(frame, (0, y), (progress, y), (0, 255, int(100 + i * 5)), 2)
            if i % 4 == 0:
                cv2.circle(frame, (progress, y), 5, (0, 255, 255), -1)
        return frame

    def draw_mode_746_decision_tree(self, frame, magnitudes):
        """Mode 746: Decision tree visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_747_support_vector_machine(self, frame, magnitudes):
        """Mode 747: Support vector machine visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_748_kernel_trick(self, frame, magnitudes):
        """Mode 748: Kernel trick visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

    def draw_mode_749_feature_space(self, frame, magnitudes):
        """Mode 749: Feature space visualization"""
        spacing = 40
        for y in range(0, self.height, spacing):
            for x in range(0, self.width, spacing):
                idx = ((y // spacing) * 20 + x // spacing) % len(magnitudes)
                mag = magnitudes[idx]
                if mag > 0.3:
                    brightness = int(100 + mag * 155)
                    cv2.rectangle(frame, (x, y), (x + int(mag * 30), y + int(mag * 30)),
                                (0, brightness, brightness), -1)
        return frame

    def draw_mode_750_dimensionality_reduction(self, frame, magnitudes):
        """Mode 750: Dimensionality reduction visualization"""
        for i, mag in enumerate(magnitudes[::4]):
            x = int((i / 30) * self.width)
            for j in range(int(mag * 20)):
                y = int(self.height - j * 15)
                alpha = 255 - j * 12
                cv2.rectangle(frame, (x, y), (x + 20, y + 10),
                            (0, alpha, int(alpha * 0.8)), -1)
        return frame

