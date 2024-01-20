import datetime


class Certificate:
    """
    Represents a certificate.
    """

    def __init__(self, name: str = "", url: str = "", github: str = "", location: str = "", beginning_date: datetime.date = None, end_date: datetime.date = None, date: datetime.date = None) -> None:
        """
        Creates a new instance of Certificate.
        :param name: Name of the certificate.
        :param url: URL of the certificate.
        :param github: GitHub repository url.
        :param location: Where the certificate was obtained.
        :param beginning_date: (Optional) Date when the certificate was obtained (beginning).
        :param end_date: (Optional) Date when the certificate was obtained (end).
        :param date: (Optional) Date when the certificate was obtained.
        """
        self.name = name
        self.url = url
        self.location = location
        self.github = github
        self.beginning_date = beginning_date
        self.end_date = end_date
        self.date = date

        # Attributing the value of beginning date
        if self.beginning_date is None:
            self.beginning_date = self.date

        # Attributing the value of end date
        if self.end_date is None:
            self.end_date = self.date

        # Attributing the value of date
        if self.date is None:
            if self.end_date is not None:
                self.date = self.end_date
            else:
                self.date = self.beginning_date

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
        string = f"\cvevent{{{self.name}}}{{"
        if (self.url is not None) and (len(self.url) > 0):
            string += f"\\cvreference{{\\faGlobe}}{{{self.url}}}"
        if (self.github is not None) and (len(self.github) > 0):
            string += f"\\cvreference{{\\faGithub}}{{{self.github}}}"
        string += f"}}{{{date}}}{{{self.location}}}"
        string += "\n\\divider"

        return string
