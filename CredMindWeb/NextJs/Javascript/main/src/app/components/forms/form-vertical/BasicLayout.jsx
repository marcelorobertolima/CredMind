import { Grid, InputAdornment, Button } from '@mui/material';
import CustomFormLabel from '../theme-elements/CustomFormLabel';
import CustomTextField from '../theme-elements/CustomTextField';
import CustomOutlinedInput from '../theme-elements/CustomOutlinedInput';

const BasicLayout = () => {
  return (
    (<div>
      {/* ------------------------------------------------------------------------------------------------ */}
      {/* Basic Layout */}
      {/* ------------------------------------------------------------------------------------------------ */}
      <Grid container>
        {/* 1 */}
        <Grid
          size={12}
          sx={{
            display: "flex",
            alignItems: "center"
          }}>
          <CustomFormLabel htmlFor="bl-name" sx={{ mt: 0 }}>
            Name
          </CustomFormLabel>
        </Grid>
        <Grid size={12}>
          <CustomTextField id="bl-name" placeholder="John Deo" fullWidth />
        </Grid>
        {/* 2 */}
        <Grid
          size={12}
          sx={{
            display: "flex",
            alignItems: "center"
          }}>
          <CustomFormLabel htmlFor="bl-company">
            Company
          </CustomFormLabel>
        </Grid>
        <Grid size={12}>
          <CustomTextField id="bl-company" placeholder="ACME Inc." fullWidth />
        </Grid>
        {/* 3 */}
        <Grid
          size={12}
          sx={{
            display: "flex",
            alignItems: "center"
          }}>
          <CustomFormLabel htmlFor="bl-email">
            Email
          </CustomFormLabel>
        </Grid>
        <Grid size={12}>
          <CustomOutlinedInput
            endAdornment={<InputAdornment position="end">@example.com</InputAdornment>}
            id="bl-email"
            placeholder="john.deo"
            fullWidth
          />
        </Grid>
        {/* 4 */}
        <Grid
          size={12}
          sx={{
            display: "flex",
            alignItems: "center"
          }}>
          <CustomFormLabel htmlFor="bl-phone">
            Phone No
          </CustomFormLabel>
        </Grid>
        <Grid size={12}>
          <CustomTextField id="bl-phone" placeholder="412 2150 451" fullWidth />
        </Grid>
        {/* 5 */}
        <Grid
          size={12}
          sx={{
            display: "flex",
            alignItems: "center"
          }}>
          <CustomFormLabel htmlFor="bl-message">
            Message
          </CustomFormLabel>
        </Grid>
        <Grid size={12}>
          <CustomTextField
            id="bl-message"
            placeholder="Hi, Do you  have a moment to talk Jeo ?"
            multiline
            fullWidth
          />
        </Grid>
        <Grid size={12} sx={{
          mt: 3
        }}>
          <Button variant="contained" color="primary">Send</Button>
        </Grid>
      </Grid>
    </div>)
  );
};

export default BasicLayout;
