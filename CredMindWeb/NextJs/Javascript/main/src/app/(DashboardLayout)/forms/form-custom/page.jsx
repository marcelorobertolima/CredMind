'use client';
import React from 'react';
import {
  Grid,
  Box,
  Typography,
  FormControl,
  RadioGroup,
  FormControlLabel,
  Button,
} from '@mui/material';
import { SliderThumb } from '@mui/material/Slider';

import Breadcrumb from '@/app/(DashboardLayout)/layout/shared/breadcrumb/Breadcrumb';
import PageContainer from '@/app/components/container/PageContainer';

import CustomTextField from '@/app/components/forms/theme-elements/CustomTextField';
import CustomRangeSlider from '@/app/components/forms/theme-elements/CustomRangeSlider';
import CustomSwitch from '@/app/components/forms/theme-elements/CustomSwitch';
import CustomDisabledButton from '@/app/components/forms/theme-elements/CustomDisabledButton';
import CustomOutlinedButton from '@/app/components/forms/theme-elements/CustomOutlinedButton';
import CustomFormLabel from '@/app/components/forms/theme-elements/CustomFormLabel';
import CustomCheckbox from '@/app/components/forms/theme-elements/CustomCheckbox';
import CustomRadio from '@/app/components/forms/theme-elements/CustomRadio';

import ParentCard from '@/app/components/shared/ParentCard';
import { IconVolume, IconVolume2 } from '@tabler/icons-react';
import { Stack } from '@mui/material';
import FormSelect from '@/app/components/forms/form-custom/FormSelect';
import FormTimePicker from '@/app/components/forms/form-custom/FormTimePicker';
import FormDate from '@/app/components/forms/form-custom/FormDate';
import FormSelectGroup from '@/app/components/forms/form-custom/FormSelectGroup';

function CustomThumbComponent(props) {
  const { children, ...other } = props;

  return (
    <SliderThumb {...other}>
      {children}
      <Box
        sx={{
          height: 9,
          width: '2px',
          backgroundColor: '#fff',
        }}
      />
      <Box
        sx={{
          height: '14px',
          width: '2px',
          backgroundColor: '#fff',
          ml: '2px',
        }}
      />
      <Box
        sx={{
          height: 9,
          width: '2px',
          backgroundColor: '#fff',
          ml: '2px',
        }}
      />
    </SliderThumb>
  );
}

export default function FormCustom() {

  return (
    (<PageContainer title="Custom Form" description="this is Custom Form">
      {/* breadcrumb */}
      <Breadcrumb title="Custom Form" subtitle="custom designed element" />
      {/* end breadcrumb */}
      <ParentCard title="Custom Form">
        <Grid container spacing={3}>
          <Grid
            size={{
              xs: 12,
              sm: 12,
              lg: 4
            }}>
            <CustomFormLabel htmlFor="name">Name</CustomFormLabel>
            <CustomTextField id="name" placeholder="Enter text" variant="outlined" fullWidth />
          </Grid>
          <Grid
            size={{
              xs: 12,
              sm: 12,
              lg: 4
            }}>
            <CustomFormLabel htmlFor="cname">Company Name</CustomFormLabel>
            <CustomTextField id="cname" placeholder="Enter text" variant="outlined" fullWidth />
          </Grid>
          <Grid
            size={{
              xs: 12,
              sm: 12,
              lg: 4
            }}>
            <CustomFormLabel htmlFor="disabled">Industry Type</CustomFormLabel>
            <CustomTextField
              id="disabled"
              placeholder="Disabled filled"
              variant="outlined"
              fullWidth
              disabled
              sx={{
                '& .MuiOutlinedInput-notchedOutline': {
                  borderColor: (theme) =>
                    `${theme.palette.mode === 'dark'
                      ? 'rgba(255, 255, 255, 0.12) !important'
                      : '#dee3e9 !important'
                    }`,
                },
              }}
            />
          </Grid>
          <Grid
            size={{
              xs: 12,
              sm: 12,
              lg: 4
            }}>
            <FormSelect />
          </Grid>
          {/* ----------------------------------- */}
          {/* column 2 */}
          {/* ----------------------------------- */}
          <Grid
            size={{
              xs: 12,
              sm: 12,
              lg: 4
            }}>
            <FormTimePicker />
          </Grid>
          {/* ----------------------------------- */}
          {/* column 3 */}
          {/* ----------------------------------- */}
          <Grid
            size={{
              xs: 12,
              sm: 12,
              lg: 4
            }}>
            <FormDate />
          </Grid>
          {/* ----------------------------------- */}
          {/* column 4 */}
          {/* ----------------------------------- */}
          <Grid
            size={{
              xs: 12,
              sm: 12,
              lg: 12
            }}>
            <CustomFormLabel>Lorem ipsum dolor sit amet</CustomFormLabel>
            <RadioGroup aria-label="gender" defaultValue="radio1" name="radio-buttons-group">
              <Grid container>
                <Grid
                  size={{
                    xs: 12,
                    sm: 4,
                    lg: 4
                  }}>
                  <FormControl component="fieldset">
                    <FormControlLabel value="radio1" control={<CustomRadio />} label="Male" />
                  </FormControl>
                </Grid>
                <Grid
                  size={{
                    xs: 12,
                    sm: 4,
                    lg: 4
                  }}>
                  <FormControl component="fieldset">
                    <FormControlLabel value="radio2" control={<CustomRadio />} label="Female" />
                  </FormControl>
                </Grid>
                <Grid
                  size={{
                    xs: 12,
                    sm: 4,
                    lg: 4
                  }}>
                  <FormControl component="fieldset">
                    <FormControlLabel
                      value="radio3"
                      control={<CustomRadio disabled />}
                      label="Disabled"
                    />
                  </FormControl>
                </Grid>
              </Grid>
            </RadioGroup>
          </Grid>
          {/* ----------------------------------- */}
          {/* column 5 */}
          {/* ----------------------------------- */}
          <Grid
            size={{
              xs: 12,
              sm: 12,
              lg: 12
            }}>
            <CustomFormLabel>Industry Type</CustomFormLabel>
            <RadioGroup aria-label="gender" defaultValue="radio1" name="radio-buttons-group">
              <Grid container>
                <Grid
                  size={{
                    xs: 12,
                    sm: 4,
                    lg: 4
                  }}>
                  <FormControlLabel
                    control={<CustomCheckbox defaultChecked />}
                    label="Enter text"
                  />
                </Grid>
                <Grid
                  size={{
                    xs: 12,
                    sm: 4,
                    lg: 4
                  }}>
                  <FormControlLabel control={<CustomCheckbox />} label="Enter text" />
                </Grid>
                <Grid
                  size={{
                    xs: 12,
                    sm: 4,
                    lg: 4
                  }}>
                  <FormControlLabel
                    disabled
                    control={<CustomCheckbox disabled />}
                    label="Disabled"
                  />
                </Grid>
              </Grid>
            </RadioGroup>
          </Grid>
          {/* ----------------------------------- */}
          {/* column 6 */}
          {/* ----------------------------------- */}
          <Grid
            size={{
              xs: 12,
              sm: 12,
              lg: 4
            }}>
            <CustomFormLabel>Slider</CustomFormLabel>
            <CustomRangeSlider
              slots={{ thumb: CustomThumbComponent }}
              getAriaLabel={(index) => (index === 0 ? 'Minimum price' : 'Maximum price')}
              defaultValue={[20, 40]}
            />

            <FormSelectGroup />


            <Box
              sx={{
                display: "flex",
                alignItems: "stretch"
              }}>
              <Typography>
                <IconVolume2 width={20} />
              </Typography>
              <Box sx={{
                ml: "auto"
              }}>
                <Typography>
                  <IconVolume width={20} />
                </Typography>
              </Box>
            </Box>
          </Grid>

          {/* ----------------------------------- */}
          {/* column 7 */}
          {/* ----------------------------------- */}

          <Grid
            size={{
              xs: 12,
              sm: 12,
              lg: 12
            }}>
            <CustomFormLabel>Switch</CustomFormLabel>
            <Grid container spacing={0}>
              <Grid
                size={{
                  xs: 12,
                  sm: 6,
                  lg: 3
                }}>
                <FormControlLabel control={<CustomSwitch />} label="Enter text" />
              </Grid>
              <Grid
                size={{
                  xs: 12,
                  sm: 6,
                  lg: 3
                }}>
                <FormControlLabel control={<CustomSwitch defaultChecked />} label="Enter text" />
              </Grid>
              <Grid
                size={{
                  xs: 12,
                  sm: 6,
                  lg: 3
                }}>
                <FormControlLabel
                  control={
                    <CustomSwitch
                      disabled
                      sx={{
                        '& .MuiSwitch-switchBase.Mui-disabled+.MuiSwitch-track': {
                          opacity: 1,
                        },
                      }}
                    />
                  }
                  label="Disabled"
                />
              </Grid>
              <Grid
                size={{
                  xs: 12,
                  sm: 6,
                  lg: 3
                }}>
                <FormControlLabel
                  control={
                    <CustomSwitch
                      defaultChecked
                      disabled
                      sx={{
                        '& .MuiSwitch-switchBase.Mui-checked.Mui-disabled': {
                          opacity: 0.5,
                        },
                      }}
                    />
                  }
                  label="Disabled"
                />
              </Grid>
            </Grid>
            {/* button */}
            <Stack
              direction={{ xs: 'column', sm: 'row' }}
              spacing={2}
              sx={{
                justifyContent: "space-between",
                mt: 2
              }}>
              <Stack spacing={1} direction="row">
                <Button variant="contained" color="primary">
                  Add New
                </Button>
                <CustomDisabledButton variant="contained" disabled>
                  Add New
                </CustomDisabledButton>
                <CustomOutlinedButton variant="outlined">Add New</CustomOutlinedButton>
              </Stack>
              <Stack direction="row" spacing={1}>
                <Button variant="contained" color="secondary">
                  Add New
                </Button>
                <Button variant="contained" color="success">
                  Add New
                </Button>
              </Stack>
            </Stack>
          </Grid>
        </Grid>
      </ParentCard>
    </PageContainer>)
  );
}
