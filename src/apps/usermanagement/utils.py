"""
Viddie is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Viddie is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

"""


def check_conditions(password: str) -> bool:
    password_check = [lambda s: any(x.isupper() for x in s), lambda s: any(x.islower() for x in s),
                      lambda s: any(x.isdigit() for x in s), lambda s: len(s) >= 8, ]

    return all(condition(password) for condition in password_check)
