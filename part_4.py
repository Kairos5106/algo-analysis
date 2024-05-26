first_letter = """To My Dearest Nefertari,
As I sit here amidst the grandeur of this
ancient pyramid, surrounded by the whispers
of the past, my thoughts turn to you, my
beloved. Though miles may separate us, know
that you are always in my heart, a beacon of
light guiding me through the darkness of the
unknown.
As I embark on this journey into the depths of
the pyramid, I am filled with a mixture of
excitement and trepidation. The allure of
uncovering ancient secrets and treasures
beckons me forward, but with each step I take,
I am reminded of the risks that accompany such endeavors.
I cannot help but think of the life we have
built together, the moments of joy and
laughter we have shared, and the love that
binds us together across time and space. It is
your unwavering support and encouragement
that give me strength in the face of
uncertainty, and for that, I am eternally
grateful.
Though the sands of time may have long since
buried the civilization that built this
magnificent structure, I find solace in the
knowledge that our love transcends the ages, a
timeless testament to the power of the human
spirit.
Until we are reunited once more, know that
you are always with me, guiding me through
the labyrinth of life with your love and light.
With all my heart,
Your devoted."""

second_letter = """To My Dearest Nefertari,
As I sit here amidst the grandeur of this
antediluvian pyramid, surrounded by the whispers of the past, my thoughts turn to you,
my beloved. Though miles may separate us,
know that you are always in my heart, a
beacon of light guiding me through the
darkness of the unknown.
As I embark on this voyage into the depths of the pyramid, I am filled with a mixture of
excitement and trepidation. The allure of
uncovering ancient secrets and treasures
beckons me forward, but with each step I take,
I am reminded of the risks that accompany
such endeavors.
I cannot help but think of the life we have
built together, the moments of joy and
laughter we have shared, and the love that
binds us together within time and space. It is your unwavering support and encouragement
that give me strength in the face of
uncertainty, and for that, I am eternally
grateful.
Though the sands of time may have long since
buried the society that built this magnificent structure, I find solace in the knowledge that
our love transcends the ages, a timeless
testament to the power of the human spirit.
Until we are reunited once more, know that
you are always with me, guiding me through
the labyrinth of life with your love and light.
With all my heart,
Your devoted"""

def minimum_edit_distance(source, target):
    m = len(source)
    n = len(target)

    # Initialize the 2D matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Traverse through the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

    return dp[m][n]

def main():
    # Test the minimum_edit_distance function
    source_text = "gay"
    target_text = "gay"
    distance = minimum_edit_distance(source_text, target_text)
    print("Minimum Edit Distance:", distance)

main()