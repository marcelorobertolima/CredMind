import CustomSocialButton from "@/app/components/forms/theme-elements/CustomSocialButton";
import { Stack } from "@mui/system";
import Avatar from '@mui/material/Avatar';
import Box from '@mui/material/Box';

const AuthSocialButtons = ({ title }) => (
  <>
    <Stack
      direction="row"
      spacing={2}
      sx={{
        justifyContent: "center",
        mt: 3
      }}>
      <CustomSocialButton>
        <Avatar
          src={"/images/svgs/google-icon.svg"}
          alt={"icon1"}
          sx={{
            width: 16,
            height: 16,
            borderRadius: 0,
            mr: 1,
          }}
        />
        <Box
          sx={{
            display: { xs: "none", sm: "flex" },
            whiteSpace: "nowrap",
            mr: { sm: "3px" },
          }}
        >
          {title}{" "}
        </Box>{" "}
        Google
      </CustomSocialButton>
      <CustomSocialButton>
        <Avatar
          src={"/images/svgs/facebook-icon.svg"}
          alt={"icon2"}
          sx={{
            width: 25,
            height: 25,
            borderRadius: 0,
            mr: 1,
          }}
        />
        <Box
          sx={{
            display: { xs: "none", sm: "flex" },
            whiteSpace: "nowrap",
            mr: { sm: "3px" },
          }}
        >
          {title}{" "}
        </Box>{" "}
        FB
      </CustomSocialButton>
    </Stack>
  </>
);

export default AuthSocialButtons;
