#!/usr/bin/env python3
# Created By: Fred
# Date: Feb 18 2008
# Display colour.


def main():

    # Colour code for red
    for red in range(0, 5):

        # Colour code for green
        for green in range(0, 120):

            # Colour code for blue
            for blue in range(0, 145):

                print(
                    "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(
                        red,
                        green,
                        blue,
                        "RGB(" + str(red) + "," + str(green) + "," + str(blue) + ")",
                    )
                )


if __name__ == "__main__":

    main()
