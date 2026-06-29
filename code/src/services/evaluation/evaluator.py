from collections import defaultdict

class Evaluator:

    def evaluate(
        self,
        predictions,
        ground_truth
    ):

        metrics = defaultdict(int)

        total = len(predictions)

        for pred, truth in zip(
            predictions,
            ground_truth
        ):

            if (
                pred.claim_status
                == truth.claim_status
            ):
                metrics["claim_status"] += 1

            if (
                pred.issue_type
                == truth.issue_type
            ):
                metrics["issue_type"] += 1

            if (
                pred.object_part
                == truth.object_part
            ):
                metrics["object_part"] += 1

            if (
                pred.severity
                == truth.severity
            ):
                metrics["severity"] += 1

        print("\n===== EVALUATION =====")

        for metric, count in metrics.items():

            accuracy = (
                count / total * 100
            )

            print(
                f"{metric}: "
                f"{accuracy:.2f}%"
            )