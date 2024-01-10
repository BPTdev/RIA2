import unittest
import os  # Vous devrez peut-être importer d'autres modules nécessaires
from AwsLabelDetectorImpl import AwsLabelDetectorImpl


class TestLabelDetector(unittest.TestCase):
    def setUp(self):
        # Définissez vos variables ici
        self.localFile = "image.png"
        self.remoteFileUrl = "URL_de_votre_fichier_distant"
        self.label_detector = AwsLabelDetectorImpl()  # Remplacez par votre classe réelle
        return super().setUp()

    def test_analyze_local_file_with_default_values_image_analyzed(self):
        # Given
        self.assertTrue(os.path.exists(self.localFile))  # Assurez-vous que localFile existe

        # When
        response = self.label_detector.analyze(self.localFile)
        # TODO: Le type de réponse contient la charge utile (retournée en JSON par l'API)

        # Then
        self.assertTrue(len(response.AmountOfLabels) <= 10)
        for metric in response.Metrics:
            self.assertTrue(metric.confidenceLevel >= 90)

    def test_analyze_remote_image_with_default_values_image_analyzed(self):
        # Given
        # TODO: Testez si le fichier distant est disponible

        # When
        response = self.label_detector.analyze(self.remoteFileUrl)
        # TODO: Le type de réponse contient la charge utile (retournée en JSON par l'API)

        # Then
        self.assertTrue(len(response.AmountOfLabels) <= 10)
        for metric in response.Metrics:
            self.assertTrue(metric.confidenceLevel >= 90)

    def test_analyze_remote_image_with_custom_max_label_value_image_analyzed(self):
        # Given
        # TODO: Testez si le fichier distant est disponible
        maxLabels = 5

        # When
        response = self.label_detector.analyze(self.remoteFileUrl, maxLabels)
        # TODO: Le type de réponse contient la charge utile (retournée en JSON par l'API)

        # Then
        self.assertTrue(len(response.AmountOfLabels) <= maxLabels)
        for metric in response.Metrics:
            self.assertTrue(metric.confidenceLevel >= 90)

    def test_analyze_remote_image_with_custom_min_confidence_level_value_image_analyzed(self):
        # Given
        # TODO: Testez si le fichier distant est disponible
        minConfidenceLevel = 60

        # When
        response = self.label_detector.analyze(self.remoteFileUrl, minConfidenceLevel)
        # TODO: Le type de réponse contient la charge utile (retournée en JSON par l'API)

        # Then
        self.assertTrue(len(response.AmountOfLabels) <= 10)
        for metric in response.Metrics:
            self.assertTrue(metric.confidenceLevel >= minConfidenceLevel)

    def test_analyze_remote_image_with_custom_values_image_analyzed(self):
        # Given
        # TODO: Testez si le fichier distant est disponible
        maxLabels = 5
        minConfidenceLevel = 60

        # When
        response = self.label_detector.analyze(self.remoteFileUrl, maxLabels, minConfidenceLevel)
        # TODO: Le type de réponse contient la charge utile (retournée en JSON par l'API)

        # Then
        self.assertTrue(len(response.AmountOfLabels) <= maxLabels)
        for metric in response.Metrics:
            self.assertTrue(metric.confidenceLevel >= minConfidenceLevel)

if __name__ == '__main__':
    unittest.main()
