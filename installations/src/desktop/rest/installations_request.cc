//  Copyright (c) 2022 Google LLC
// 
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// 
//      http://www.apache.org/licenses/LICENSE-2.0
// 
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
#include "installations/src/desktop/rest/installations_request.h"

#include "app/src/app_common.h"

namespace firebase {
namespace installations {
namespace internal {
InstallationsRequest::InstallationsRequest(const char* schema)
    : RequestJson(schema) {
  add_header(app_common::kApiClientHeader, App::GetUserAgent());
}
}  // namespace internal
}  // namespace installations
}  // namespace firebase