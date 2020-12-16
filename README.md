# To do:
- ~~access MangaUpdates' API~~ no API afaik
- get top-N latest / 1st page
- error handling
  - check for valid `perpage` or `page` values
- threading?

## Concrete To-do list:
- [x] Extend argument `page=N` to `page=[1, 2, 5, ...]` or `page=range(10)`
- [ ] Use more memory-efficient algorithm to select entries (e.g. `find_next`)
- [ ] Extract all useful information from each entry (e.g. links)
- [ ] Make function to scrape the actual pages of the manga entries
- [ ] Verbose flag
