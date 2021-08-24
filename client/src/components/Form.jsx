import React from 'react'
import Typography from '@material-ui/core/Typography'
import Slider from '@material-ui/core/Slider'
import { useHistory, useLocation } from 'react-router-dom'

function valuetext(value) {
  return `${value}$`
}

const formField = {
  province__iexact: '',                 // Assign province name
  city__iexact: '',                     // Assign city name
  rent_per_month__lte: '',              // Assign max rent
  rent_per_month__gte: '',              // Assign min rent
  extra_expenses_per_month__lte: '',     // Assign max extra expenses
  extra_expenses_per_month__gte: '',     // Assign min extra expenses
  earliest_move_in_date__iexact: '',    // Assign a date
  length_of_lease__lte: '',             // Assign max length
  length_of_lease__gte: '',             // Assign min length
  room_type: '',                        // Assign roomy type
  is_furnished: '',                     // Assign furnished checkbox value
  is_laundry_ensuite: '',               // Assign ensuite laundry checkbox value
  is_air_conditioned: '',               // Assign air conditioned checkbox value
  poster__university__iexact: '',       // Assign poster's univeristy value
  poster__university_major__iexact: '', // Assign poster's university major value
  poster__profession__iexact: '',       // Assign poster's profession value
  rent_per_month_sort: '',              // If user selects ascending assign rent_per_month as value if descending -rent_per_month
  length_of_lease_sort: '',             // If user selects ascending assign rent_per_month as value if descending -length_of_lease_sort
  earliest_move_in_date_sort: '',       // If user selects ascending assign rent_per_month as value if descending -earliest_move_in_date_sort
}

//Note if ordering selected at all. We should only allow the user to order by one of the three sort properties
//?ordering=rent_per_month
// ?ordering=-rent_per_month

//Here is an example of what the url should look like if I just queried province as Ontario
// api/listings/?province__iexact=Ontario&city__iexact=&rent_per_month__lte=&rent_per_month__gte=&extra_expenses_per_month__lte=&extra_expenses_per_month__gte=&earliest_move_in_date__iexact=&length_of_lease__lte=&length_of_lease__gte=&room_type=&is_furnished=&is_air_conditioned=&is_laundry_ensuite=&poster__university__iexact=&poster__university_major__iexact=&poster__profession__iexact=

// Here is an example of what the url should look like if I queried province as Ontario and set ordering for rent per month as ascending
//api/listings/?city__iexact=&earliest_move_in_date__iexact=&extra_expenses_per_month__gte=&extra_expenses_per_month__lte=&is_air_conditioned=&is_furnished=&is_laundry_ensuite=&length_of_lease__gte=&length_of_lease__lte=&ordering=rent_per_month&poster__profession__iexact=&poster__university__iexact=&poster__university_major__iexact=&province__iexact=Ontario&rent_per_month__gte=&rent_per_month__lte=&room_type=

const Form = () => {
  // const classes = useStyles();
  const history = useHistory()
  const { search } = useLocation()

  // Slider states
  const [RentSlider, setRentSlider] = React.useState([600, 1250])
  const [ExtraExpensesSlider, setExtraExpensesSlider] = React.useState([20, 60])
  const [LengthLeaseSlider, setLengthLeaseSlider] = React.useState([4, 12])
  
  // rent range slider function
  const handleChange = (event, newValue) => {
    setRentSlider(newValue)
  }
  const handleMinRent = (e) => {
    setRentSlider([e.target.value, RentSlider[1]])
  }
  const handleMaxRent = (e) => {
    setRentSlider([RentSlider[0], e.target.value])
  }

  // expenses slider function
  const handleExtraExpensesSlider = (event, newValue) => {
    setExtraExpensesSlider(newValue)
  }
  const handleMinExpenses = (e) => {
    setExtraExpensesSlider([e.target.value, ExtraExpensesSlider[1]])
  }
  const handleMaxExpenses = (e) => {
    setExtraExpensesSlider([ExtraExpensesSlider[0], e.target.value])
  }

  // length lease slider function
  const handleLengthLeaseSlider = (event, newValue) => {
    setLengthLeaseSlider(newValue)
  }
  const handleMaxlease = (e) => {
    setLengthLeaseSlider([LengthLeaseSlider[0], e.target.value])
  }
  const handleMinlease = (e) => {
    setLengthLeaseSlider([e.target.value, LengthLeaseSlider[1]])
  }

  // input field values and select function
  const [inputValues, setInputValues] = React.useState(formField)
  const handleInputSelect = (event) => {
    setInputValues({ ...inputValues, [event.target.name]: event.target.value })
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    setInputValues(formField)
  }

  return (
    <div className="form_container">
      <div className="form_md">
        <div className="head">
          <h2>Field Filters</h2>
        </div>
        <form
          // onSubmit={handleSubmit}
          action="http://localhost:3002/formData"
          className="filter_form"
        >
          <div className="inputs">
            <label htmlFor="province">
              Province
              <br />
              <input
                type="text"
                name="province"
                id="province"
                placeholder="Province"
                required
                value={inputValues.province}
                onChange={handleInputSelect}
              />
            </label>
          </div>
          <div className="inputs">
            <label htmlFor="city">
              City
              <br />
              <input
                type="text"
                name="city"
                id="city"
                placeholder="City"
                required
                onChange={handleInputSelect}
              />
            </label>
          </div>
          <div className="inputs">
            <Typography id="range-slider" gutterBottom>
              Rent per Month
            </Typography>
            <div className="range_boxes">
              <label htmlFor="">
                <input
                  type="text"
                  value={`${RentSlider[0]}`}
                  onChange={handleMinRent}
                />
              </label>
              <label htmlFor="">
                <input
                  type="text"
                  value={`${RentSlider[1]}`}
                  onChange={handleMaxRent}
                />
              </label>
            </div>
            <Slider
              value={RentSlider}
              onChange={handleChange}
              name="rent_per_month_range"
              valueLabelDisplay="auto"
              aria-labelledby="range-slider"
              getAriaValueText={valuetext}
              min={0}
              max={5000}
            />
          </div>

          <div className="inputs">
            <Typography id="range-slider" gutterBottom>
              Additional Expenses per Month
            </Typography>
            <div className="range_boxes">
              <label htmlFor="">
                <input
                  type="text"
                  value={`${ExtraExpensesSlider[0]}`}
                  onChange={handleMinExpenses}
                />
              </label>
              <label htmlFor="">
                <input
                  type="text"
                  value={`${ExtraExpensesSlider[1]}`}
                  onChange={handleMaxExpenses}
                />
              </label>
            </div>
            <Slider
              value={ExtraExpensesSlider}
              onChange={handleExtraExpensesSlider}
              name="extra_expenses_per_month"
              valueLabelDisplay="auto"
              aria-labelledby="range-slider"
              getAriaValueText={valuetext}
              min={0}
              max={500}
            />
          </div>
          <div className="inputs">
            <label htmlFor="extra_expenses_per_month_gte">
              Earliest Move-in Date
              <br />
              <input
                type="date"
                name="earliest_move_in_date"
                id="earliest_move_in_date"
                required
                onChange={handleInputSelect}
              />
            </label>
          </div>

          <div className="inputs">
            <Typography id="range-slider" gutterBottom>
              Length of Lease
            </Typography>
            <div className="range_boxes">
              <label htmlFor="">
                <input
                  type="text"
                  value={`${LengthLeaseSlider[0]}`}
                  onChange={handleMinlease}
                />
              </label>
              <label htmlFor="">
                <input
                  type="text"
                  value={`${LengthLeaseSlider[1]}`}
                  onChange={handleMaxlease}
                />
              </label>
            </div>
            <Slider
              value={LengthLeaseSlider}
              onChange={handleLengthLeaseSlider}
              valueLabelDisplay="auto"
              aria-labelledby="range-slider"
              getAriaValueText={valuetext}
              min={0}
              max={12}
            />
          </div>
          <div className="inputs">
            <label htmlFor="room_type">
              Room type
              <br />
              <select
                name="room_type"
                required
                id="room_type"
                onChange={handleInputSelect}
              >
                <option value="unknow">Choose a room type</option>
                <option value="Bedroom">Bedroom</option>
                <option value="Shared Bedroom">Shared Bedroom</option>
                <option value="Den">Den</option>
                <option value="Living Room">Living Room</option>
                <option value="Shared Living Room">Shared Living Room</option>
                <option value="Sunroom">Sunroom</option>
                <option value="Closet">Closet</option>
              </select>
            </label>
          </div>
          <div className="inputs">
            <label htmlFor="is_furnished">
              <input
                className="inp_check"
                type="checkbox"
                name="is_furnished"
                id="is_furnished"
                onChange={handleInputSelect}
              />
              Furnished
            </label>
          </div>
          <div className="inputs">
            <label htmlFor="is_air_conditioned">
              <input
                className="inp_check"
                type="checkbox"
                name="is_air_conditioned"
                id="is_air_conditioned"
                onChange={handleInputSelect}
              />
              Air Conditioned
            </label>
          </div>
          <div className="inputs">
            <label htmlFor="is_laundry_ensuite">
              <input
                className="inp_check"
                type="checkbox"
                name="is_laundry_ensuite"
                id="is_laundry_ensuite"
                onChange={handleInputSelect}
              />
              Ensuite Laundry
            </label>
          </div>
          <div className="inputs">
            <label htmlFor="poster_uni">
              Poster's University
              <br />
              <input
                type="text"
                name="poster_uni"
                id="poster_uni"
                required
                onChange={handleInputSelect}
              />
            </label>
          </div>
          <div className="inputs">
            <label htmlFor="poster_uni_major">
              Poster's University Major
              <br />
              <input
                type="text"
                name="poster_uni_major"
                id="poster_uni_major"
                required
                onChange={handleInputSelect}
              />
            </label>
          </div>
          <div className="inputs">
            <label htmlFor="poster_profession">
              Poster's Profession
              <br />
              <input
                type="text"
                name="poster_profession"
                id="poster_profession"
                required
                onChange={handleInputSelect}
              />
            </label>
          </div>
          <div className="inputs">
            <label htmlFor="rent_per_month_sort">
              Rent per Month Ascending/Descending
              <br />
              <select
                name="rent_per_month_sort"
                id="rent_per_month_sort"
                onChange={handleInputSelect}
                required
              >
                <option value="">Choose Ascending/Descending</option>
                <option value="ascending">Ascending &#8593; </option>
                <option value="descending">Descending &#8595; </option>
              </select>
            </label>
          </div>
          <div className="inputs">
            <label htmlFor="rent_per_month_sort">
              Length of Lease Ascending/Descending
              <br />
              <select
                name="length_of_lease_sort"
                id="length_of_lease_sort"
                onChange={handleInputSelect}
                required
              >
                <option value="">Choose Ascending/Descending</option>
                <option value="ascending">Ascending &#8593; </option>
                <option value="descending">Descending &#8595; </option>
              </select>
            </label>
          </div>
          <div className="inputs">
            <label htmlFor="rent_per_month_sort">
              Earliest Move-in Date Ascending/Descending
              <br />
              <select
                name="earliest_move_in_date_sort"
                id="earliest_move_in_date_sort"
                onChange={handleInputSelect}
                required
              >
                <option value="">Choose Ascending/Descending</option>
                <option value="ascending">Ascending &#8593; </option>
                <option value="descending">Descending &#8595; </option>
              </select>
            </label>
          </div>
          <button type="submit" className="submit_btn">
            Submit
          </button>
        </form>
      </div>
    </div>
  )
}

export default Form