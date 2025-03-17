using System.Diagnostics;

int? BinarySearch(List<int> the_list, int search_item)
{
    var low = 0;
    var high = the_list.Count() - 1;

    while (low <= high)
    {
        var mid = (high + low) / 2;
        var guess = the_list[mid];

        if (guess == search_item)
        {
            return guess;
        }

        if (guess < search_item)
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }

    return null;
}

List<int> the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

var to_find = 4;

var result = BinarySearch(the_list, to_find);

Debug.Assert(result == to_find, $"result {result} does not match expected");

Console.WriteLine(result);
