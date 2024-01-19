import datetime


class Certificate:
    """
    Represents a certificate.
    """

    def __init__(self, name: str = "", url: str = "", location: str = "", beginning_date: datetime.date = None, end_date: datetime.date = None, date: datetime.date = None) -> None:
        """
        Creates a new instance of Certificate.
        :param name: Name of the certificate.
        :param url: URL of the certificate.
        :param location: Where the certificate was obtained.
        :param beginning_date: (Optional) Date when the certificate was obtained (beginning).
        :param end_date: (Optional) Date when the certificate was obtained (end).
        :param date: (Optional) Date when the certificate was obtained.
        """
        self.name = name
        self.url = url
        self.location = location

        # Attributing the value of beginning date
        if beginning_date is not None:
            self.beginning_date = beginning_date
        else:
            self.beginning_date = date

        # Attributing the value of end date
        if end_date is not None:
            self.end_date = end_date
        else:
            self.end_date = date

    def to_latex(self) -> str:
        """
        Converts a certificate to a LaTeX string.
        :return: LaTeX string obtained from a certificate instance.
        """

        # Generating date string
        if self.beginning_date == self.end_date:
            date = self.beginning_date.strftime("%Y-%m-%d")
        else:
            date = self.beginning_date.strftime("%Y-%m-%d") + " -- " + self.end_date.strftime("%Y-%m-%d")

        # Generating final string
        return f"\\cvevent{{{self.name}}}{{\\cvreference{{\\faGlobe}}{{{self.url}}}}}{{{date}}}{{{self.location}}}\n\\divider"
