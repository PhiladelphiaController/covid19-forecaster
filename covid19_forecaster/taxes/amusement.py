from .core import ScenarioForecast
import numpy as np


class AmusementTax(ScenarioForecast):
    """
    Amusement tax revenue forecast.
    """

    ASSUMPTIONS = {
        "moderate": np.concatenate(
            [
                np.repeat(0.7, 3),
                np.repeat(0.4, 3),
                np.repeat(0.25, 3),
                np.repeat(0.15, 12),
            ]
        ),
        "severe": np.concatenate(
            [
                np.repeat(0.9, 3),
                np.repeat(0.6, 3),
                np.repeat(0.3, 3),
                np.repeat(0.2, 3),
                np.repeat(0.15, 9),
            ]
        ),
    }

    @property
    def tax_name(self):
        return "amusement"

    def get_forecasted_decline(self, scenario, date, sector=None):
        """
        Return the forecasted decline.

        Parameters
        ----------
        scenario : str
            the scenario to projct
        date : pandas.Timestamp
            the date object for the month to forecast
        """
        # Verify input
        assert scenario in ["moderate", "severe"]

        # monthly offset
        month_offset = self.get_month_offset(date)

        return self.ASSUMPTIONS[scenario][month_offset]

    def save_to_template(self):
        """
        Save the forecast to a template Excel spreadsheet.
        """
        super().save_to_template("Amusement Scenario Analysis", 31)
