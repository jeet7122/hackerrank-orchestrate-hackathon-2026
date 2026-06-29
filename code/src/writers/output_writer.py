import csv


class OutputWriter:

    HEADERS = [
        "user_id",
        "image_paths",
        "user_claim",
        "claim_object",
        "evidence_standard_met",
        "evidence_standard_met_reason",
        "risk_flags",
        "issue_type",
        "object_part",
        "claim_status",
        "claim_status_justification",
        "supporting_image_ids",
        "valid_image",
        "severity"
    ]

    def open(self, output_path):

        self.file = open(
            output_path,
            "w",
            newline="",
            encoding="utf-8"
        )

        self.writer = csv.DictWriter(
            self.file,
            fieldnames=self.HEADERS
        )

        self.writer.writeheader()

    def write_row(self, result):

        self.writer.writerow(
            result.__dict__
        )

        self.file.flush()

    def close(self):

        self.file.close()
    
    def open_append(self, output_path):

        self.file = open(
            output_path,
            "a",
            newline="",
            encoding="utf-8"
        )

        self.writer = csv.DictWriter(
            self.file,
            fieldnames=self.HEADERS
        )